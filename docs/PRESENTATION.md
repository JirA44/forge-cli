# forge-cli — Présentation

**One-liner:** 3 outils Git du quotidien en une CLI installable `pip install forge-cli`.

## À quoi ça sert ?
- **Équipe qui démarre un repo** → `forge ignore python,node,vscode` récupère le template officiel gitignore.io, évite les `__pycache__` committés.
- **Lead qui audite** → `forge stats ./repo` affiche en 1s : nb commits, fichiers suivis, top auteurs — sans ouvrir GitHub.
- **Nettoyage masse** → `forge rename ./photos --strip-accents --regex " " --replace "-"` normalise 500 fichiers avant import.

## Exemples d'utilisation
```bash
# 1) Nouveau projet Python + Node
forge ignore python,node,macos -o .gitignore

# 2) Audit rapide avant soutenance
forge stats D:/Code/forge_portfolio/V1.07/proofforge

# 3) Photos avec accents → ASCII + préfixe date
forge rename ./vacances --strip-accents --prefix 2026_ --dry-run
forge rename ./vacances --strip-accents --prefix 2026_

# 4) Renommer .jpeg → .jpg partout
forge rename ./images --regex "\.jpeg$" --replace ".jpg"
```

## Public cible
Dévs / étudiants / ops — qui veulent 0 config, 0 compte, 1 binaire.

## Roadmap publique
- [ ] `forge ignore --list` (lister templates)
- [ ] `forge stats --since 1.month`
- [ ] `forge rename --lowercase`
