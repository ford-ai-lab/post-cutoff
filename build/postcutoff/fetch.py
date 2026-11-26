"""HTTP fetching with an on-disk cache. Standard library only."""
import hashlib
import json
import os
import time
import urllib.error
import urllib.request

USER_AGENT = "post-cutoff-build/0.1"


class FetchError(Exception):
    def __init__(self, url, status, reason=""):
        super().__init__(f"{status} {reason} for {url}".strip())
        self.url, self.status, self.reason = url, status, reason


class Fetcher:
    def __init__(self, cache_dir, offline=False, delay=0.15, max_age_hours=20):
        self.cache_dir, self.offline, self.delay = cache_dir, offline, delay
        self.max_age = max_age_hours * 3600
        self.requests = 0
        os.makedirs(cache_dir, exist_ok=True)

    def _path(self, url):
        return os.path.join(self.cache_dir, hashlib.sha256(url.encode()).hexdigest()[:32])

    def get(self, url, headers=None):
        """Return the body as text. Raises FetchError (status 0 = network problem)."""
        path = self._path(url)
        meta = path + ".meta"
        if os.path.exists(meta):
            m = json.load(open(meta))
            fresh = self.offline or time.time() - m["at"] < self.max_age
            if fresh:
                if m["status"] != 200:
                    raise FetchError(url, m["status"], "cached")
                return open(path, encoding="utf-8", errors="replace").read()
        if self.offline:
            raise FetchError(url, 0, "offline and not cached")
        h = {"User-Agent": USER_AGENT}
        h.update(headers or {})
        time.sleep(self.delay)
        self.requests += 1
        status, body = 0, b""
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=h), timeout=120) as r:
                status, body = r.status, r.read()
        except urllib.error.HTTPError as e:
            status = e.code
        except Exception as e:  # network, TLS, proxy
            raise FetchError(url, 0, type(e).__name__)
        json.dump({"url": url, "status": status, "at": time.time()}, open(meta, "w"))
        if status != 200:
            raise FetchError(url, status)
        open(path, "wb").write(body)
        return body.decode("utf-8", errors="replace")

    def get_json(self, url, headers=None):
        return json.loads(self.get(url, headers))
