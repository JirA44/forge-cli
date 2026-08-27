import subprocess
from pathlib import Path
from collections import Counter

def git_stats(path: Path) -> dict:
    def run(*a): return subprocess.check_output(a, cwd=path, text=True, errors="ignore")
    try:
        log = run("git","log","--pretty=format:%an","--no-merges")
        authors = Counter(log.splitlines())
        commits = len(log.splitlines())
    except: authors, commits = {}, 0
    try:
        files = len(run("git","ls-files").splitlines())
    except: files = 0
    return {"commits": commits, "authors": dict(authors), "files": files}
