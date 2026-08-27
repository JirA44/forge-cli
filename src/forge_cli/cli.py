import click, re, unicodedata
from pathlib import Path
from .gitignore import fetch_gitignore
from .stats import git_stats
from .rename import mass_rename

@click.group()
def main(): pass

@main.command("ignore")
@click.argument("templates", nargs=-1, required=True)
@click.option("-o","--output", default=".gitignore")
def ignore_cmd(templates, output):
    content = fetch_gitignore(list(templates))
    Path(output).write_text(content, encoding="utf-8")
    click.echo(f"✓ .gitignore ← {', '.join(templates)} ({len(content)} chars) → {output}")

@main.command("stats")
@click.argument("path", default=".")
def stats_cmd(path):
    s = git_stats(Path(path))
    click.echo(f"Commits: {s['commits']}  Auteurs: {len(s['authors'])}  Fichiers: {s['files']}")
    for a,n in sorted(s["authors"].items(), key=lambda x:-x[1])[:10]:
        click.echo(f"  {a:<30} {n:>5}")

@main.command("rename")
@click.argument("directory")
@click.option("--prefix", default="")
@click.option("--regex", default="")
@click.option("--replace", default="")
@click.option("--strip-accents", is_flag=True)
@click.option("--dry-run", is_flag=True)
def rename_cmd(directory, prefix, regex, replace, strip_accents, dry_run):
    ops = mass_rename(Path(directory), prefix=prefix, regex=regex, replace=replace, strip_accents=strip_accents, dry_run=dry_run)
    for src,dst in ops:
        click.echo(f"{'[DRY] ' if dry_run else ''}{src.name} → {dst.name}")
    if not dry_run: click.echo(f"✓ {len(ops)} renommés")
