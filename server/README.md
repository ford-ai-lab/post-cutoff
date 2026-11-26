# The hosted MCP server

`mcp.js` is the function behind https://ford-lab.vercel.app/mcp (Streamable HTTP, stateless, no account).
Tools: `list_packages`, `changes_since`, `check_lockfile`.

It has no dependencies. It reads `data/post-cutoff/index.json` and `digests.json`, which are exported from the
digests in `skills/`. To use the hosted copy, add `https://ford-lab.vercel.app/mcp` as a remote MCP server in
your client. To run your own, deploy `mcp.js` as a Node serverless function (it is written for Vercel) with
those two data files beside it.
