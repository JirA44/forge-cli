import re, unicodedata
from pathlib import Path
def mass_rename(directory: Path, prefix="", regex="", replace="", strip_accents=False, dry_run=False):
    ops=[]
    pat=re.compile(regex) if regex else None
    for p in directory.iterdir():
        if not p.is_file(): continue
        name=p.name
        if strip_accents: name="".join(c for c in unicodedata.normalize("NFD",name) if unicodedata.category(c)!="Mn")
        if pat: name=pat.sub(replace, name)
        if prefix: name=prefix+name
        dst=p.with_name(name)
        if dst!=p:
            ops.append((p,dst))
            if not dry_run: p.rename(dst)
    return ops
