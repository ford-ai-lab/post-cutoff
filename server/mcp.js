// Post-cutoff: a remote MCP server over Streamable HTTP, stateless, JSON responses only (no SSE).
// Endpoint: https://ford-lab.vercel.app/api/mcp (also /mcp through a rewrite in vercel.json).
//
// It serves both protocol eras on the one endpoint ("dual-era" in the 2026-07-28 specification):
//   - Modern, 2026-07-28: no handshake. Every POST carries MCP-Protocol-Version and Mcp-Method headers
//     (Mcp-Name too for tools/call) and params._meta["io.modelcontextprotocol/protocolVersion"] and
//     ["io.modelcontextprotocol/clientCapabilities"]. Methods: server/discover, tools/list, tools/call.
//   - Legacy, 2025-11-25 and earlier: initialize, notifications/initialized, ping, tools/list, tools/call.
// Specification pages this follows (read 2026-11-26):
//   https://modelcontextprotocol.io/specification/2026-07-28/basic/transports/streamable-http
//   https://modelcontextprotocol.io/specification/2026-07-28/basic/versioning
//   https://modelcontextprotocol.io/specification/2025-11-25/basic/transports
// No dependencies. Data is read from data/post-cutoff/*.json, written by lab/post-cutoff/export_for_site.py
// and shipped with the function through "includeFiles" in vercel.json.
// One log line per tool call, starting MCP_CALL. No IP addresses and no lockfile contents are logged.
import { readFileSync } from "node:fs";
import { randomBytes } from "node:crypto";
import path from "node:path";
import { fileURLToPath } from "node:url";

const SERVER = { name: "post-cutoff", title: "Post-cutoff: what changed in your libraries", version: "0.1.0" };
const MODERN = ["2026-07-28"];
const LEGACY = ["2025-11-25", "2025-06-18", "2025-03-26", "2024-11-05"];
const SUPPORTED = [...MODERN, ...LEGACY];
const K_VERSION = "io.modelcontextprotocol/protocolVersion";
const K_CAPS = "io.modelcontextprotocol/clientCapabilities";
const K_CLIENT = "io.modelcontextprotocol/clientInfo";
const K_SERVER = "io.modelcontextprotocol/serverInfo";
const PAGE = "https://ford-lab.vercel.app/post-cutoff";
const CONTACT = "ford@readableforms.com";
const MAX_BODY = 1024 * 1024;          // request body, bytes
const MAX_LOCKFILE = 600 * 1024;       // characters of pasted file that are read
const MAX_REPLY = 48000;               // characters in a check_lockfile reply
const LIST_TTL_MS = 3600000;

// ---------------------------------------------------------------- data

let cache = null;
function data() {
  if (cache) return cache;
  const dirs = [path.join(process.cwd(), "data", "post-cutoff")];
  try { dirs.push(path.join(path.dirname(fileURLToPath(import.meta.url)), "..", "data", "post-cutoff")); } catch (e) { /* no import.meta.url */ }
  let lastError;
  for (const dir of dirs) {
    try {
      const index = JSON.parse(readFileSync(path.join(dir, "index.json"), "utf8"));
      const digests = JSON.parse(readFileSync(path.join(dir, "digests.json"), "utf8"));
      const byName = new Map();
      for (const row of index.list) {
        const key = normalise(row.ecosystem, row.name);
        if (!byName.has(key)) byName.set(key, []);
        byName.get(key).push(row);
      }
      cache = { index, digests: digests.digests, byName };
      return cache;
    } catch (e) { lastError = e; }
  }
  throw new Error("digest data not found: " + (lastError && lastError.message));
}

// PyPI names compare case-insensitively with runs of - _ . treated as one hyphen; npm names are lower case.
function normalise(ecosystem, name) {
  const n = String(name).trim().toLowerCase();
  return ecosystem === "pypi" ? n.replace(/[-_.]+/g, "-") : n;
}

function find(name, ecosystem) {
  const d = data();
  const out = [];
  for (const eco of ecosystem ? [ecosystem] : ["npm", "pypi"]) {
    for (const row of d.byName.get(normalise(eco, name)) || []) if (row.ecosystem === eco && !out.includes(row)) out.push(row);
  }
  return out;
}

function versionKey(v) { return String(v).replace(/^v/i, "").split(/[.+-]/).map((x) => parseInt(x, 10)).filter((x) => !Number.isNaN(x)); }
function versionCompare(a, b) {
  const x = versionKey(a), y = versionKey(b);
  for (let i = 0; i < Math.max(x.length, y.length); i++) {
    const d = (x[i] || 0) - (y[i] || 0);
    if (d) return d;
  }
  return 0;
}

// ---------------------------------------------------------------- tools

const TOOLS = [
  {
    name: "list_packages",
    title: "List covered packages",
    description: "List the npm and PyPI packages this server has change digests for, with each package's latest stable version, how many breaking / removed / deprecated / new entries were extracted, and the date the data was built. Call this first to see whether a library is covered.",
    inputSchema: {
      type: "object",
      properties: { ecosystem: { type: "string", enum: ["npm", "pypi"], description: "Limit the list to one ecosystem." } },
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "changes_since",
    title: "What changed in a package",
    description: "What changed in one npm or PyPI package after a date or version: breaking changes, removed or renamed APIs, deprecations, raised minimum versions and new APIs, each quoted from the package's own release notes with version, date and source link. Use it before writing or upgrading code that uses the package, because training data may describe an older API. Coverage starts 2025-06-01. Lines are picked by keyword rules, not reviewed; a package with thin release notes says so.",
    inputSchema: {
      type: "object",
      properties: {
        package: { type: "string", description: "Package name as published, for example vite, @angular/core, pandas." },
        ecosystem: { type: "string", enum: ["npm", "pypi"], description: "Needed only when the name exists in both registries (openai, langchain, playwright)." },
        since: { type: "string", description: "Only releases after this. Either a date (YYYY-MM-DD or YYYY-MM, for example your training cut-off) or a version (for example 7.0.0, the one installed). Default: everything after 2025-06-01." },
      },
      required: ["package"],
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
  {
    name: "check_lockfile",
    title: "Check a dependency file",
    description: "Paste the contents of a package.json, package-lock.json, requirements.txt, pyproject.toml, Pipfile, poetry.lock, uv.lock, yarn.lock or pnpm-lock.yaml. Returns breaking changes, removals, deprecations and raised minimum versions since 2025-06-01 for every covered package found in it, plus the names found that are not covered. The reply is capped; use changes_since for one package in full. The pasted text is not stored or logged.",
    inputSchema: {
      type: "object",
      properties: { text: { type: "string", description: "The file contents, as text." } },
      required: ["text"],
      additionalProperties: false,
    },
    annotations: { readOnlyHint: true, openWorldHint: false },
  },
];

class ToolInputError extends Error {}

function provenance(meta) {
  return `Data built ${meta.built}; covers releases after ${meta.cutoff}. Every entry is a quote from the package's own release notes, picked by keyword rules and not reviewed by a person. Open the source link before relying on a line; anything released after ${meta.built} is not here.`;
}

function listPackages(args) {
  const { index } = data();
  const eco = args.ecosystem;
  if (eco !== undefined && eco !== "npm" && eco !== "pypi") throw new ToolInputError('ecosystem must be "npm" or "pypi".');
  const rows = index.list.filter((r) => !eco || r.ecosystem === eco);
  const out = [`# Post-cutoff: ${rows.length} covered packages${eco ? " (" + eco + ")" : ""}`, "", provenance(index), "",
    "Columns: package | ecosystem | latest stable (date) | breaking / removed-or-renamed / deprecated / minimum-version / new entries extracted | note", ""];
  for (const r of rows) {
    const c = r.counts;
    const note = r.status === "items" ? "" : ` | no entries: ${r.status}`;
    out.push(`- ${r.name} | ${r.ecosystem} | ${r.latest || "unknown"}${r.latest_date ? " (" + r.latest_date + ")" : ""} | ${c.breaking}/${c.removed}/${c.deprecated}/${c.minver}/${c.new}${note}`);
  }
  out.push("", `Call changes_since with a package name for its digest. A package that is missing can be requested: ${CONTACT} (${PAGE}).`);
  return { text: out.join("\n"), log: { package: null } };
}

function parseSince(since, cutoff) {
  if (since === undefined || since === null || since === "") return null;
  if (typeof since !== "string") throw new ToolInputError("since must be a string: a date (YYYY-MM-DD or YYYY-MM) or a version (for example 7.0.0).");
  const s = since.trim();
  let m = /^(\d{4})-(\d{2})(?:-(\d{2}))?$/.exec(s);
  if (m) {
    const date = `${m[1]}-${m[2]}-${m[3] || "01"}`;
    if (Number.isNaN(Date.parse(date + "T00:00:00Z"))) throw new ToolInputError(`since: ${s} is not a real date.`);
    return { kind: "date", value: date, early: date < cutoff };
  }
  m = /^v?(\d+(?:\.\d+){0,3})([-+.][0-9A-Za-z.-]*)?$/.exec(s);
  if (m && !/^\d{5,}$/.test(m[1])) return { kind: "version", value: m[1] };
  throw new ToolInputError(`since: could not read ${JSON.stringify(s.slice(0, 40))}. Give a date (YYYY-MM-DD or YYYY-MM) or a version (for example 7.0.0).`);
}

// Render one digest. opts.since filters release groups; opts.cats limits categories; opts.perSection caps entries.
function renderDigest(d, meta, opts = {}) {
  const since = opts.since || null;
  const out = [];
  let shown = 0, hidden = 0;
  for (const sec of d.sections) {
    if (opts.cats && !opts.cats.includes(sec.cat)) continue;
    const groups = sec.groups.filter((g) => {
      if (!since) return true;
      if (since.kind === "date") return !/^\d{4}-\d{2}-\d{2}$/.test(g.d) || g.d > since.value;
      return versionCompare(g.v, since.value) > 0;
    });
    hidden += sec.groups.reduce((n, g) => n + g.items.length, 0) - groups.reduce((n, g) => n + g.items.length, 0);
    if (!groups.length) continue;
    const lines = [];
    let left = opts.perSection || Infinity, cut = 0;
    for (const g of groups) {
      const take = g.items.slice(0, Math.max(0, left));
      cut += g.items.length - take.length;
      if (!take.length) continue;
      lines.push(`### ${g.v} (${g.d}) source: ${g.src}`);
      for (const t of take) lines.push(`- ${t}`);
      left -= take.length;
      shown += take.length;
    }
    out.push(`## ${sec.title}`, ...lines);
    const more = sec.omitted + cut;
    if (more > 0) out.push(`- (${more} more in this category not shown${cut ? " here; changes_since gives more" : ""}; see the changelog.)`);
    out.push("");
  }
  return { lines: out, shown, hidden };
}

function changesSince(args) {
  const { index, digests } = data();
  if (typeof args.package !== "string" || !args.package.trim()) throw new ToolInputError("package is required: a package name such as vite or pandas.");
  const name = args.package.trim().slice(0, 120);
  const eco = args.ecosystem;
  if (eco !== undefined && eco !== "npm" && eco !== "pypi") throw new ToolInputError('ecosystem must be "npm" or "pypi".');
  const since = parseSince(args.since, index.cutoff);
  const rows = find(name, eco);
  const log = { package: name.replace(/[^\w@./-]/g, "").slice(0, 80), covered: rows.length > 0 };
  if (!rows.length) {
    const other = eco ? find(name, eco === "npm" ? "pypi" : "npm") : [];
    const key = name.toLowerCase().replace(/^@/, "");
    const near = index.list.filter((r) => { const n = r.name.toLowerCase(); return n.includes(key) || (key.length > 3 && key.includes(n.replace(/^@/, ""))); }).slice(0, 6);
    const out = [`"${name}" is not covered${eco ? " for " + eco : ""}. This server has digests for ${index.packages} packages (call list_packages); for anything else read the package's own changelog.`];
    if (other.length) out.push(`It is covered for ${other[0].ecosystem}: call again with ecosystem "${other[0].ecosystem}".`);
    else if (near.length) out.push("Covered names that look similar: " + near.map((r) => `${r.name} (${r.ecosystem})`).join(", ") + ".");
    out.push(`To have it added, write to ${CONTACT} (${PAGE}).`);
    return { text: out.join("\n"), log };
  }
  const out = [];
  for (const row of rows) {
    const d = digests[`${row.ecosystem}/${row.name}`];
    out.push(`# ${d.name} (${d.ecosystem}): changes after ${since ? (since.kind === "date" ? since.value : "version " + since.value) : index.cutoff}`, "");
    for (const h of d.header) out.push(`- ${h}`);
    if (since && since.kind === "date" && since.early) out.push(`- You asked for changes since ${since.value}. This data starts at ${index.cutoff}; releases between the two dates are not covered here.`);
    out.push("");
    const r = renderDigest(d, index, { since });
    out.push(...r.lines);
    if (since && r.hidden) out.push(`(${r.hidden} entries from releases at or before ${since.value} are left out.)`, "");
    if (!r.shown && d.sections.length) out.push(`No extracted entry is newer than ${since.value}.`, "");
    if (d.notes.length) { out.push("## Changes"); for (const n of d.notes) out.push(`- ${n}`); out.push(""); }
    out.push("## Coverage");
    for (const c of d.coverage) out.push(`- ${c}`);
    out.push("");
  }
  out.push(provenance(index));
  return { text: out.join("\n"), log };
}

// ---- dependency file parsing: returns [{ ecosystem, name, spec }] with duplicates removed

function pep508(s) {
  const m = /^\s*([A-Za-z0-9][A-Za-z0-9._-]*)\s*(?:\[[^\]]*\])?\s*([^;#]*)/.exec(s);
  if (!m) return null;
  return { name: m[1], spec: m[2].trim().replace(/^\(|\)$/g, "").slice(0, 40) };
}

function parseDependencyText(text) {
  const found = [];
  const add = (ecosystem, name, spec) => { if (name && name.length <= 214) found.push({ ecosystem, name: String(name), spec: typeof spec === "string" ? spec.slice(0, 40) : "" }); };
  let kind = "unknown";
  const trimmed = text.trimStart();
  if (trimmed.startsWith("{")) {
    let j = null;
    try { j = JSON.parse(text); } catch (e) { /* fall through to the text scans */ }
    if (j && typeof j === "object") {
      if (j.default || j.develop) {                                    // Pipfile.lock
        kind = "Pipfile.lock";
        for (const sec of [j.default, j.develop]) if (sec && typeof sec === "object") for (const [n, v] of Object.entries(sec)) add("pypi", n, v && v.version);
      } else if (j.packages && typeof j.packages === "object" && !Array.isArray(j.packages)) {   // package-lock v2/v3
        kind = "package-lock.json";
        const root = j.packages[""] || {};
        const direct = { ...root.dependencies, ...root.devDependencies, ...root.optionalDependencies, ...root.peerDependencies };
        if (Object.keys(direct).length) {
          for (const n of Object.keys(direct)) { const p = j.packages["node_modules/" + n]; add("npm", n, (p && p.version) || direct[n]); }
        } else {
          for (const [k, p] of Object.entries(j.packages)) { const i = k.lastIndexOf("node_modules/"); if (i === 0) add("npm", k.slice(13), p && p.version); }
        }
      } else {
        kind = j.lockfileVersion ? "package-lock.json" : "package.json";
        for (const f of ["dependencies", "devDependencies", "peerDependencies", "optionalDependencies"]) {
          if (j[f] && typeof j[f] === "object") for (const [n, v] of Object.entries(j[f])) add("npm", n, typeof v === "string" ? v : v && v.version);
        }
      }
    }
  }
  const lines = text.split(/\r?\n/);
  if (kind === "unknown" && /^\s*\[\[?[A-Za-z0-9_.\-"' ]+\]\]?\s*(#.*)?$/m.test(text)) {    // TOML: pyproject, Pipfile, poetry.lock, uv.lock
    kind = /^\s*\[\[package\]\]/m.test(text) ? "Python lock file" : /^\s*\[(dev-)?packages\]/m.test(text) ? "Pipfile" : "pyproject.toml";
    let table = "", inDeps = false, lockName = null;
    for (const raw of lines) {
      const line = raw.trim();
      if (!line || line.startsWith("#")) continue;
      let m = /^\[\[?([^\]]+)\]\]?\s*(#.*)?$/.exec(line);
      if (m && !inDeps) { table = m[1].trim().replace(/["']/g, ""); lockName = null; continue; }
      if (inDeps) {
        for (const q of line.matchAll(/"([^"]+)"|'([^']+)'/g)) { const p = pep508(q[1] || q[2]); if (p) add("pypi", p.name, p.spec); }
        if (/\]\s*(#.*)?$/.test(line.replace(/"[^"]*"|'[^']*'/g, ""))) inDeps = false;
        continue;
      }
      m = /^([A-Za-z0-9_.-]+|"[^"]+")\s*=\s*(.*)$/.exec(line);
      if (!m) continue;
      const key = m[1].replace(/"/g, ""), value = m[2];
      if (table === "package") {                                         // poetry.lock, uv.lock
        if (key === "name") lockName = value.replace(/["']/g, "").trim();
        if (key === "version" && lockName) { add("pypi", lockName, value.replace(/["']/g, "").trim()); lockName = null; }
        continue;
      }
      const arrayTable = (table === "project" && key === "dependencies") || table === "project.optional-dependencies" || table === "dependency-groups"
        || (table === "tool.uv" && key === "dev-dependencies") || table === "tool.pdm.dev-dependencies";
      if (arrayTable && value.startsWith("[")) {
        for (const q of value.matchAll(/"([^"]+)"|'([^']+)'/g)) { const p = pep508(q[1] || q[2]); if (p) add("pypi", p.name, p.spec); }
        if (!/\]\s*(#.*)?$/.test(value.replace(/"[^"]*"|'[^']*'/g, ""))) inDeps = true;
        continue;
      }
      if (/(^|\.)(dev-)?dependencies$/.test(table) && table.startsWith("tool.poetry") || table === "packages" || table === "dev-packages") {
        if (key.toLowerCase() !== "python") add("pypi", key, (/"([^"]*)"/.exec(value) || [])[1] || "");
      }
    }
  }
  if (kind === "unknown" && (/^# yarn lockfile|^__metadata:/m.test(text) || /^lockfileVersion:/m.test(text))) {
    kind = /^lockfileVersion:/m.test(text) ? "pnpm-lock.yaml" : "yarn.lock";
    for (const raw of lines) {
      let m = /^"?(@?[^@\s",]+)@(?:npm:)?([^",:]+)/.exec(raw);                           // yarn: name@range:
      if (m && raw.trimEnd().endsWith(":")) { add("npm", m[1], m[2]); continue; }
      m = /^ {2,8}'?\/?((?:@[a-z0-9][a-z0-9._-]*\/)?[a-z0-9][a-z0-9._-]*)'?:\s*$/.exec(raw);        // pnpm importers: "      name:"
      if (m && !/^(dependencies|devDependencies|optionalDependencies|specifiers|packages|importers|snapshots|resolution|engines|peerDependencies|settings|overrides|catalogs?|default|transitivePeerDependencies|peerDependenciesMeta|bin|cpu|os)$/.test(m[1])) { add("npm", m[1], ""); continue; }
      m = /^ {2,4}'?\/?((?:@[a-z0-9][a-z0-9._-]*\/)?[a-z0-9][a-z0-9._-]*)@(\d[^'(:]*)/.exec(raw);    // pnpm packages: "  name@1.2.3:"
      if (m) add("npm", m[1], m[2]);
    }
  }
  if (kind === "unknown") {                                                                // requirements.txt style
    kind = "requirements.txt";
    for (const raw of lines) {
      const line = raw.split(/\s+#/)[0].trim();
      if (!line || line.startsWith("#") || line.startsWith("-") || /^[a-z+]+:\/\//i.test(line)) continue;
      const p = pep508(line);
      if (p && /^[A-Za-z0-9._-]+\s*(\[[^\]]*\])?\s*($|[<>=!~;@ ])/.test(line)) add("pypi", p.name, p.spec);
    }
  }
  const seen = new Map();
  for (const f of found) {
    const key = f.ecosystem + "/" + normalise(f.ecosystem, f.name);
    if (!seen.has(key)) seen.set(key, f);
    else if (!seen.get(key).spec && f.spec) seen.get(key).spec = f.spec;
  }
  return { kind, deps: [...seen.values()] };
}

function checkLockfile(args) {
  const { index, digests } = data();
  if (typeof args.text !== "string" || !args.text.trim()) throw new ToolInputError("text is required: paste the contents of package.json, requirements.txt, pyproject.toml or a lockfile.");
  const truncatedInput = args.text.length > MAX_LOCKFILE;
  const { kind, deps } = parseDependencyText(truncatedInput ? args.text.slice(0, MAX_LOCKFILE) : args.text);
  const covered = [], missing = [];
  for (const dep of deps) {
    const row = find(dep.name, dep.ecosystem)[0];
    if (row) covered.push({ dep, row }); else missing.push(dep);
  }
  const log = { package: null, kind, found: deps.length, covered: covered.length };
  if (!deps.length) {
    return { text: `No dependency names could be read from that text (read as ${kind}). Paste the whole file: package.json, package-lock.json, requirements.txt, pyproject.toml, Pipfile, poetry.lock, uv.lock, yarn.lock or pnpm-lock.yaml.`, isError: true, log };
  }
  const weight = (r) => r.counts.breaking + r.counts.removed + r.counts.minver;
  covered.sort((a, b) => (weight(b.row) > 0) - (weight(a.row) > 0));
  const head = [`# Dependency check (read as ${kind})`, "",
    `${deps.length} dependency names found; ${covered.length} are covered by this server, ${missing.length} are not.`, provenance(index),
    "Apply only entries whose version is at or below the version the project has installed; later entries describe an upgrade it has not made. New-feature entries are left out here: call changes_since for one package in full.", ""];
  if (truncatedInput) head.push(`Only the first ${MAX_LOCKFILE} characters of the text were read.`, "");
  const tail = [];
  if (missing.length) {
    const names = missing.slice(0, 60).map((m) => m.name);
    tail.push("## Not covered", names.join(", ") + (missing.length > 60 ? ` and ${missing.length - 60} more` : "") + ".",
      `These have no digest here; read their own changelogs. Packages can be added on request, private and internal ones included: ${CONTACT} (${PAGE}).`, "");
  }
  // Keep room for a one-line summary of every covered package, so none goes unmentioned when digests are cut.
  let budget = MAX_REPLY - head.join("\n").length - tail.join("\n").length - 200 - covered.length * 170;
  const body = [], brief = [];
  for (const { dep, row } of covered) {
    const d = digests[`${row.ecosystem}/${row.name}`];
    const block = [`# ${d.name} (${d.ecosystem})${dep.spec ? " - this file says " + dep.spec : ""}`];
    block.push(`- Latest stable: ${d.latest || "unknown"}${d.latest_date ? " (" + d.latest_date + ")" : ""}.` + (d.majors.length ? " New major versions since the cut-off: " + d.majors.map((m) => `${m[0]} (${m[1]})`).join(", ") + "." : ""));
    const r = renderDigest(d, index, { cats: ["breaking", "removed", "deprecated", "minver"], perSection: 8 });
    if (r.shown) block.push("", ...r.lines);
    else block.push(`- ${d.status === "items" ? "No breaking change, removal, deprecation or minimum-version entry was extracted (" + d.counts.new + " new-feature entries; see changes_since)." : "No entries: " + d.status + ". " + (d.notes[0] || "")}`, "");
    const size = block.join("\n").length + 1;
    if (size <= budget) { body.push(...block); budget -= size; }
    else brief.push(`- ${d.name} (${d.ecosystem}): latest ${d.latest || "unknown"}; ${d.counts.breaking} breaking, ${d.counts.removed} removed or renamed, ${d.counts.deprecated} deprecated, ${d.counts.minver} minimum-version entries. Call changes_since.`);
  }
  if (brief.length) body.push("## Covered, but left out of this reply to keep it short", ...brief, "");
  return { text: [...head, ...body, ...tail].join("\n").trimEnd(), log };
}

const RUN = { list_packages: listPackages, changes_since: changesSince, check_lockfile: checkLockfile };

// ---------------------------------------------------------------- JSON-RPC and HTTP

const clean = (s, n) => String(s === undefined || s === null ? "" : s).replace(/[^\x20-\x7e]/g, "").slice(0, n);

class RpcError extends Error {
  constructor(code, message, status, dataField) { super(message); this.code = code; this.status = status; this.data = dataField; }
}

function header(req, name) {
  const v = req.headers[name.toLowerCase()];
  return Array.isArray(v) ? v[0] : v;
}

// Mcp-Name may arrive as =?base64?...?= when the value is not plain ASCII (2026-07-28, "Value Encoding").
function decodeHeaderValue(v) {
  const m = /^=\?base64\?([A-Za-z0-9+/=]*)\?=$/.exec(v);
  return m ? Buffer.from(m[1], "base64").toString("utf8") : v;
}

// Origin. The specification requires servers to validate Origin and answer 403 when it is present and invalid
// (the threat is DNS rebinding against servers that hold local data or trust ambient credentials). This server
// is public, read-only, has no authentication and sets no cookies, so every well-formed http(s) or editor
// web-view origin is accepted and anything else that is present is refused, including "null". Setting
// MCP_ALLOWED_ORIGINS (comma-separated origins) restricts it to that list.
function originAllowed(origin) {
  if (origin === undefined || origin === "") return true;
  const allow = (process.env.MCP_ALLOWED_ORIGINS || "").split(",").map((s) => s.trim()).filter(Boolean);
  if (allow.length) return allow.includes(origin);
  if (origin.length > 300 || /[\s<>"'`\\]/.test(origin)) return false;
  let u;
  try { u = new URL(origin); } catch (e) { return false; }
  if (!["http:", "https:", "vscode-webview:", "vscode-file:"].includes(u.protocol)) return false;
  if (u.username || u.password || !u.host) return false;
  return (u.pathname === "/" || u.pathname === "") && !u.search && !u.hash;
}

function readBody(req) {
  let parsed;
  try { parsed = req.body; } catch (e) { return Promise.reject(new RpcError(-32700, "Parse error: the body is not valid JSON", 400)); }   // Vercel's lazy parser throws on bad JSON
  if (parsed !== undefined && parsed !== null) {
    if (Buffer.isBuffer(parsed)) return Promise.resolve(parsed.toString("utf8"));
    return Promise.resolve(parsed);          // an object (already parsed) or a string
  }
  return new Promise((resolve, reject) => {
    let size = 0;
    const chunks = [];
    req.on("data", (c) => {
      size += c.length;
      if (size > MAX_BODY) { reject(new RpcError(-32600, "Request too large", 413)); req.destroy(); return; }
      chunks.push(c);
    });
    req.on("end", () => resolve(Buffer.concat(chunks).toString("utf8")));
    req.on("error", () => reject(new RpcError(-32700, "Could not read the request body", 400)));
  });
}

function send(res, status, body) {
  res.statusCode = status;
  if (body === undefined) { res.end(); return; }
  res.setHeader("Content-Type", "application/json");
  res.end(JSON.stringify(body));
}

const fail = (res, id, e) => send(res, e.status || 200, { jsonrpc: "2.0", id: id === undefined ? null : id, error: { code: e.code, message: e.message, ...(e.data ? { data: e.data } : {}) } });

const INSTRUCTIONS = "Release-note digests for popular npm and PyPI packages, covering releases after 2025-06-01. Before writing or upgrading code that uses a covered package, call changes_since (or check_lockfile with the project's dependency file) and apply only entries at or below the installed version. Entries are keyword-filtered quotes from upstream release notes, not reviewed; open the source link before relying on one.";

// Legacy clients are told who they are only at initialize, and this server keeps no state. The session id it
// hands out therefore carries the client's name, so later tool calls can be logged with it. It grants nothing.
function mintSession(clientInfo) {
  const name = clean(clientInfo && clientInfo.name, 40), version = clean(clientInfo && clientInfo.version, 20);
  return "pc1." + Buffer.from(JSON.stringify([name, version])).toString("base64url") + "." + randomBytes(9).toString("base64url");
}
function clientFromSession(id) {
  const m = /^pc1\.([A-Za-z0-9_-]{1,200})\.[A-Za-z0-9_-]+$/.exec(id || "");
  if (!m) return null;
  try { const a = JSON.parse(Buffer.from(m[1], "base64url").toString("utf8")); return clean(a[0], 40) + (a[1] ? "/" + clean(a[1], 20) : ""); } catch (e) { return null; }
}

function callTool(req, params, client) {
  if (!params || typeof params.name !== "string") throw new RpcError(-32602, "Invalid params: tools/call needs params.name");
  const run = RUN[params.name];
  if (!run) throw new RpcError(-32602, `Unknown tool: ${clean(params.name, 60)}`);
  const args = params.arguments === undefined || params.arguments === null ? {} : params.arguments;
  if (typeof args !== "object" || Array.isArray(args)) throw new RpcError(-32602, "Invalid params: arguments must be an object");
  let out;
  try { out = run(args); } catch (e) {
    if (!(e instanceof ToolInputError)) throw e;
    out = { text: e.message, isError: true, log: { package: typeof args.package === "string" ? clean(args.package, 80) : null } };
  }
  console.log("MCP_CALL " + JSON.stringify({ tool: params.name, package: null, ...out.log, ua: clean(header(req, "user-agent"), 120), client: client || null, error: out.isError ? true : undefined }));
  return { content: [{ type: "text", text: out.text }], isError: out.isError === true };
}

function handleModern(req, res, msg) {
  const id = msg.id, params = msg.params && typeof msg.params === "object" ? msg.params : {};
  const meta = params._meta && typeof params._meta === "object" ? params._meta : {};
  const bodyVersion = meta[K_VERSION], headVersion = header(req, "mcp-protocol-version");
  if (typeof bodyVersion !== "string") throw new RpcError(-32602, `Invalid params: _meta["${K_VERSION}"] is required`, 400);
  if (headVersion === undefined) throw new RpcError(-32020, "Header mismatch: the MCP-Protocol-Version header is required", 400);
  if (headVersion !== bodyVersion) throw new RpcError(-32020, `Header mismatch: MCP-Protocol-Version header value '${clean(headVersion, 20)}' does not match body value '${clean(bodyVersion, 20)}'`, 400);
  if (!MODERN.includes(bodyVersion)) throw new RpcError(-32022, "Unsupported protocol version", 400, { supported: SUPPORTED, requested: clean(bodyVersion, 20) });
  if (meta[K_CAPS] === null || typeof meta[K_CAPS] !== "object") throw new RpcError(-32602, `Invalid params: _meta["${K_CAPS}"] is required`, 400);
  const headMethod = header(req, "mcp-method");
  if (headMethod === undefined) throw new RpcError(-32020, "Header mismatch: the Mcp-Method header is required", 400);
  if (headMethod !== msg.method) throw new RpcError(-32020, `Header mismatch: Mcp-Method header value '${clean(headMethod, 40)}' does not match body value '${clean(msg.method, 40)}'`, 400);
  const done = (result) => send(res, 200, { jsonrpc: "2.0", id, result: { resultType: "complete", ...result, _meta: { [K_SERVER]: SERVER } } });
  if (msg.method === "server/discover") {
    return done({ supportedVersions: SUPPORTED, capabilities: { tools: {} }, instructions: INSTRUCTIONS, ttlMs: LIST_TTL_MS, cacheScope: "public" });
  }
  if (msg.method === "tools/list") return done({ tools: TOOLS, ttlMs: LIST_TTL_MS, cacheScope: "public" });
  if (msg.method === "tools/call") {
    const headName = header(req, "mcp-name");
    if (headName === undefined) throw new RpcError(-32020, "Header mismatch: the Mcp-Name header is required for tools/call", 400);
    if (decodeHeaderValue(headName) !== params.name) throw new RpcError(-32020, `Header mismatch: Mcp-Name header value '${clean(headName, 60)}' does not match body value '${clean(params.name, 60)}'`, 400);
    const ci = meta[K_CLIENT];
    const client = ci && typeof ci === "object" && ci.name ? clean(ci.name, 40) + (ci.version ? "/" + clean(ci.version, 20) : "") : null;
    return done(callTool(req, params, client));
  }
  const hint = msg.method === "initialize" || msg.method === "ping" ? ` (not part of protocol version ${bodyVersion}; this server also supports ${LEGACY.join(", ")})` : "";
  throw new RpcError(-32601, `Method not found: ${clean(msg.method, 60)}${hint}`, 404);
}

function handleLegacy(req, res, msg) {
  const id = msg.id, params = msg.params && typeof msg.params === "object" ? msg.params : {};
  const done = (result) => send(res, 200, { jsonrpc: "2.0", id, result });
  if (msg.method === "initialize") {
    const asked = params.protocolVersion;
    const version = LEGACY.includes(asked) ? asked : LEGACY[0];      // same version if supported, else the newest handshake version
    const ci = params.clientInfo && typeof params.clientInfo === "object" ? params.clientInfo : null;
    res.setHeader("Mcp-Session-Id", mintSession(ci));
    console.log("MCP_INIT " + JSON.stringify({ client: ci ? clean(ci.name, 40) + (ci.version ? "/" + clean(ci.version, 20) : "") : null, asked: clean(asked, 20), version, ua: clean(header(req, "user-agent"), 120) }));
    return done({ protocolVersion: version, capabilities: { tools: { listChanged: false } }, serverInfo: SERVER, instructions: INSTRUCTIONS });
  }
  const headVersion = header(req, "mcp-protocol-version");
  if (headVersion !== undefined && !LEGACY.includes(headVersion)) {
    throw new RpcError(-32022, "Unsupported protocol version", 400, { supported: SUPPORTED, requested: clean(headVersion, 20) });
  }
  if (msg.method === "ping") return done({});
  if (msg.method === "tools/list") return done({ tools: TOOLS });
  if (msg.method === "tools/call") return done(callTool(req, params, clientFromSession(header(req, "mcp-session-id"))));
  throw new RpcError(-32601, `Method not found: ${clean(msg.method, 60)}`);
}

export default async function handler(req, res) {
  const origin = header(req, "origin");
  res.setHeader("Cache-Control", "no-store");
  res.setHeader("X-Content-Type-Options", "nosniff");
  res.setHeader("Vary", "Origin");
  if (!originAllowed(origin)) return fail(res, null, new RpcError(-32600, "Forbidden: Origin not allowed", 403));
  res.setHeader("Access-Control-Allow-Origin", origin || "*");
  res.setHeader("Access-Control-Expose-Headers", "Mcp-Session-Id");
  if (req.method === "OPTIONS") {
    res.setHeader("Access-Control-Allow-Methods", "POST, OPTIONS");
    res.setHeader("Access-Control-Allow-Headers", clean(header(req, "access-control-request-headers"), 400) || "Content-Type, Accept, MCP-Protocol-Version, Mcp-Method, Mcp-Name, Mcp-Session-Id");
    res.setHeader("Access-Control-Max-Age", "86400");
    return send(res, 204);
  }
  if (req.method !== "POST") {
    // No standalone SSE stream (GET) and no sessions to end (DELETE): 405 in every supported revision.
    res.setHeader("Allow", "POST, OPTIONS");
    return fail(res, null, new RpcError(-32600, "Method not allowed: this MCP endpoint accepts POST only (no SSE stream, no sessions)", 405));
  }
  let id = null;
  try {
    if (!/^application\/json\b/i.test(String(header(req, "content-type") || ""))) throw new RpcError(-32600, "Unsupported media type: send Content-Type: application/json", 415);
    const accept = String(header(req, "accept") || "*/*");
    if (!/application\/json|application\/\*|\*\/\*/i.test(accept)) throw new RpcError(-32600, "Not acceptable: the Accept header must allow application/json", 406);
    if (Number(header(req, "content-length") || 0) > MAX_BODY) throw new RpcError(-32600, "Request too large", 413);
    let msg = await readBody(req);
    if (typeof msg === "string") {
      if (Buffer.byteLength(msg, "utf8") > MAX_BODY) throw new RpcError(-32600, "Request too large", 413);
      try { msg = JSON.parse(msg); } catch (e) { throw new RpcError(-32700, "Parse error: the body is not valid JSON", 400); }
    }
    if (Array.isArray(msg)) throw new RpcError(-32600, "Invalid request: JSON-RPC batches are not supported; send one message per POST", 400);
    if (!msg || typeof msg !== "object" || msg.jsonrpc !== "2.0") throw new RpcError(-32600, 'Invalid request: expected a JSON-RPC 2.0 object ("jsonrpc": "2.0")', 400);
    const hasId = Object.prototype.hasOwnProperty.call(msg, "id");
    if (hasId && msg.id !== null && typeof msg.id !== "string" && typeof msg.id !== "number") throw new RpcError(-32600, "Invalid request: id must be a string or a number", 400);
    if (typeof msg.method !== "string") {
      if (hasId && (Object.prototype.hasOwnProperty.call(msg, "result") || Object.prototype.hasOwnProperty.call(msg, "error"))) return send(res, 202);   // a client's response to a server request: none are ever sent, accept and drop
      throw new RpcError(-32600, "Invalid request: method is required", 400);
    }
    if (!hasId || msg.id === null) return send(res, 202);            // a notification (notifications/initialized, notifications/cancelled, ...)
    id = msg.id;
    const headVersion = header(req, "mcp-protocol-version");
    const bodyVersion = msg.params && typeof msg.params === "object" && msg.params._meta && typeof msg.params._meta === "object" ? msg.params._meta[K_VERSION] : undefined;
    if (msg.method !== "initialize" && headVersion !== undefined && !SUPPORTED.includes(headVersion) && bodyVersion === undefined) {
      throw new RpcError(-32022, "Unsupported protocol version", 400, { supported: SUPPORTED, requested: clean(headVersion, 20) });
    }
    // Era: an initialize request or a handshake-era version header selects legacy behaviour; per-request
    // metadata, a modern version header or server/discover selects the stateless 2026-07-28 behaviour.
    const legacy = msg.method === "initialize" ? !(MODERN.includes(headVersion) || bodyVersion !== undefined)
      : LEGACY.includes(headVersion) ? true
        : !(headVersion !== undefined || bodyVersion !== undefined || msg.method === "server/discover");
    return legacy ? handleLegacy(req, res, msg) : handleModern(req, res, msg);
  } catch (e) {
    if (e instanceof RpcError) return fail(res, id, e);
    console.error("MCP_ERROR " + clean(e && e.message, 200));
    return fail(res, id, new RpcError(-32603, "Internal error", 500));
  }
}
