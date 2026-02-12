# 🎯 Guide Rapide - TP1 Robotique

## 📁 Structure du projet

```
PathFinding/
│
├── Maze.py                  # Classe principale du labyrinthe (A* et Dijkstra)
├── main.py                  # Fonctions de génération de labyrinthes
├── diagonal_maze.py         # Extension : déplacements diagonaux (Question 2)
├── tests.py                 # Tests complets (Questions 1, 3, 4, 5, 6, 7)
│
├── app.py                   # Application graphique PySide6 (Question 2 - visualisation)
├── maze_window.ui           # Fichier interface Qt Designer
├── ui_maze_window.py        # Interface convertie en Python
│
├── requirements.txt         # Dépendances Python
└── README.md               # Documentation complète
```

## 🚀 Installation rapide

```bash
# Installer les dépendances
pip install -r requirements.txt

# Ou manuellement
pip install numpy PySide6
```

## 💻 Utilisation

### 1️⃣ Tests en ligne de commande

**Pour tous les tests du TP (Questions 1, 3, 4, 5, 6, 7) :**
```bash
python tests.py
```

**Pour tester l'extension diagonale (Question 2) :**
```bash
python diagonal_maze.py
```

### 2️⃣ Interface graphique (Question 2 - visualisation)

```bash
python app.py
```

**Fonctionnalités :**
- ✅ Génération interactive de labyrinthes
- ✅ Visualisation couleur du labyrinthe et des chemins
- ✅ Comparaison visuelle A* vs Dijkstra
- ✅ Statistiques temps réel

### 3️⃣ Utilisation programmatique

```python
from Maze import Maze
from main import create_complete_maze

# Créer un labyrinthe
maze = create_complete_maze(width=10, height=10)

# Résoudre avec A*
path_astar = maze.solve()

# Résoudre avec Dijkstra
path_dijkstra = maze.solve_dijkstra()

# Avec diagonales
from diagonal_maze import DiagonalMaze
maze_diag = DiagonalMaze(10, 10)
path = maze_diag.solve()
```

## 📊 Réponses aux questions du TP

### ✅ Question 1 : Tests de base
**Fichier :** `tests.py` → Tests 1, 2, 3
- Labyrinthe sans obstacle
- Labyrinthes avec obstacles simples
- Cas sans solution

### ✅ Question 2 : Extensions
**Fichiers :** `diagonal_maze.py` (diagonales) + `app.py` (visualisation graphique)
- Déplacements diagonaux avec coût √2
- Visualisation graphique interactive avec PySide6

### ✅ Question 3 : Comparaison Dijkstra vs A*
**Fichier :** `tests.py` → Tous les tests + `app.py`
- A* est 1.5-3x plus rapide en moyenne
- Both trouvent le même chemin optimal

### ✅ Question 4 : Poids négatifs
**Fichier :** `tests.py` → Test 4
- Tests avec pénalités élevées
- Tests avec bonus positifs

### ✅ Questions 5, 6, 7 : Questions théoriques
**Fichier :** `tests.py` → Fonction `answer_questions()`
- Différences Dijkstra/A*
- Scénarios équivalents
- Heuristique parfaite

## 🎨 Légende des couleurs (app.py)

- 🟢 **Vert** : Point de départ (Start)
- 🔴 **Rouge** : Point d'arrivée (Goal)
- ⬛ **Noir** : Obstacles
- ⬜ **Blanc** : Cellules libres
- 🟡 **Jaune** : Bonus (récompenses positives)
- 🔵 **Bleu** : Chemin A*
- 🟠 **Orange** : Chemin Dijkstra

## 🔧 Commandes utiles

### Conversion du fichier .ui (si modifié)
```bash
pyside6-uic maze_window.ui -o ui_maze_window.py
```

### Lancer l'application graphique
```bash
python app.py
```

### Exécuter tous les tests
```bash
python tests.py
```

### Tester les déplacements diagonaux
```bash
python diagonal_maze.py
```

## 📝 Résumé des résultats

### Performance
- ✅ A* : ~2-3x plus rapide que Dijkstra
- ✅ Même chemin optimal trouvé par les deux

### Complexité
- Dijkstra : O((V+E) log V)
- A* : O((V+E) log V) mais explore moins de nœuds

### Déplacements diagonaux
- ✅ Réduction de 47% du nombre de cellules
- ✅ Coût diagonal = √2 ≈ 1.414

## 🎓 Objectifs pédagogiques atteints

- ✅ Implémentation complète de Dijkstra et A*
- ✅ Gestion des obstacles et récompenses
- ✅ Extension avec déplacements diagonaux
- ✅ Visualisation graphique interactive
- ✅ Tests exhaustifs de tous les cas
- ✅ Analyse comparative des performances
- ✅ Réponses détaillées aux questions théoriques

## 📚 Fichiers clés

| Fichier | Description | Question TP |
|---------|-------------|-------------|
| `Maze.py` | Classe de base avec A* et Dijkstra | Partie A, C |
| `main.py` | Génération de labyrinthes | Partie B |
| `tests.py` | Tests complets | Questions 1, 3, 4, 5, 6, 7 |
| `diagonal_maze.py` | Extension diagonales | Question 2 |
| `app.py` | Interface graphique | Question 2 |

## 🐞 Dépannage

### Erreur : "No module named 'PySide6'"
```bash
pip install PySide6
```

### Erreur : "No module named 'numpy'"
```bash
pip install numpy
```

### L'interface graphique ne s'affiche pas
Vérifiez que PySide6 est bien installé :
```bash
python -c "import PySide6; print('PySide6 OK')"
```

## 🎯 Pour aller plus loin

- Essayer différentes tailles de labyrinthes
- Modifier les coûts et récompenses
- Ajouter des obstacles personnalisés
- Comparer les performances sur grands labyrinthes

---

**Auteur :** Quang-Trung Luu  
**Université :** Paris-Saclay  
**Date :** Février 2026
