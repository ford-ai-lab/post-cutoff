"""SUMMARISER HOOK. Nothing in this file calls a model.

The pipeline is deterministic: classify.py picks upstream sentences, render.py prints them.
If you want a model to compress a release further, set

    POST_CUTOFF_SUMMARISER=some_module:some_function

and the build will call  some_function(package, release)  once per release, after the
deterministic extraction. `release.blocks` holds the upstream text, `release.items` the
(category, text) pairs already extracted. Return a list of (category, text) pairs to
replace them, or None to keep them.

Rules a summariser must keep, because the skill promises them to its readers:
  * every statement must be supported by release.blocks; no outside knowledge;
  * if the notes are thin, return [] so the digest says "no details in release notes";
  * anything it writes is labelled as machine-summarised in the output (render.py does this).
"""
import importlib
import os


def load():
    spec = os.environ.get("POST_CUTOFF_SUMMARISER")
    if not spec:
        return None
    module, _, func = spec.partition(":")
    return getattr(importlib.import_module(module), func)


def apply(hook, package, release):
    if hook is None:
        return False
    result = hook(package, release)
    if result is None:
        return False
    release.items = [(c, t) for c, t in result]
    return True
