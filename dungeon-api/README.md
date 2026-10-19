# Dungeon as a Service — starter

Squelette fourni pour le projet bonus du module Python Backend & FastAPI.

## Installation (à faire une seule fois)

Prérequis : Python 3.10 ou plus récent (`python --version`).

```bash
# 1. Créer et activer un environnement virtuel
python -m venv .venv
# Windows (PowerShell) :
.venv\Scripts\Activate.ps1
# macOS / Linux :
source .venv/bin/activate

# 2. Installer les dépendances
pip install -r requirements.txt
```

## Lancer l'API

Depuis la racine du projet (le dossier qui contient `app/`) :

```bash
fastapi dev app/main.py
```

Ouvrez ensuite http://127.0.0.1:8000/docs : la route `GET /health` doit répondre
`{"status": "ok", ...}`. Si c'est le cas, vous êtes prêts.

## Structure

```
app/
  main.py              point d'entrée, branchement des routers
  database.py          connexion SQLite (FOURNI)
  models/              tables SQLModel
  schemas/             schémas Pydantic d'entrée et de sortie
  domain/              classes métier (Heros, Guerrier, Mage, Voleur)
  services/            logique du jeu
    dungeon_map.py     lecture de la carte (FOURNI)
  routes/              routers FastAPI
data/dungeon_map.json  carte du donjon (FOURNI, ne pas modifier)
client/play.py         client terminal (BONUS)
```

## Réinitialiser la partie

Arrêtez le serveur et supprimez le fichier `dungeon.db` : il sera recréé au prochain lancement.
À faire aussi si vous ajoutez une colonne à une table (SQLite ne met pas à jour une table existante).

---

<!-- À COMPLÉTER PAR LE GROUPE AVANT LE RENDU -->

## Notre rendu

- **Membres du groupe :** Béatrix de Almeida 
- **Lien du dépôt Git :** https://github.com/Beadlm/DaaS/
- **Palier atteint :**  4
- **Bonus réalisés :** trop fatiguée
- **Ce qui ne fonctionne pas / difficultés :** Adapter ce qu'on nous a appris dans un nouvel environnement (fichier main séparé des routes). Avoir à faire des choses (tables bdd et login) d'une manière non apprise en cours. Réussire a tester après le système de login car il ne nous as pas été expliqué correctement en cours et donc ceci reste un concept plutot abstrait (surtout pour une personne neurodivergente) dû au manque de pratique externe (jamais login sur swagger avant) et de vraies explications de concepts (les exercices sur Yquest n'expliquent rien juste demandent à faire)
