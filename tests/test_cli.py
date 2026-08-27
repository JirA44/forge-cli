from pathlib import Path
from forge_cli.rename import mass_rename
def test_mass_rename(tmp_path):
    (tmp_path/"café.txt").write_text("x")
    ops=mass_rename(tmp_path, strip_accents=True, dry_run=True)
    assert ops[0][1].name=="cafe.txt"
def test_prefix(tmp_path):
    (tmp_path/"a.txt").write_text("x")
    ops=mass_rename(tmp_path, prefix="pre-", dry_run=True)
    assert ops[0][1].name=="pre-a.txt"
