import numpy as np
import heapq


class Maze:
    """
    Classe représentant un labyrinthe avec obstacles, récompenses et points de départ/arrivée.
    """
   
    def __init__(self, width, height, grid=None, rewards=None, start=None, goal=None):
        """
        Initialise un labyrinthe.
       
        Args:
            width (int): Largeur du labyrinthe (nombre de colonnes)
            height (int): Hauteur du labyrinthe (nombre de lignes)
            grid (np.ndarray, optional): Grille des obstacles (0 = libre, 1 = obstacle)
            rewards (np.ndarray, optional): Matrice de récompense
            start (tuple, optional): Coordonnées du point de départ (ligne, colonne)
            goal (tuple, optional): Coordonnées du point d'arrivée (ligne, colonne)
        """
        self.width = width
        self.height = height
       
        # Initialisation de la grille (0 = libre, 1 = obstacle)
        if grid is None:
            self.grid = np.zeros((height, width), dtype=int)
        else:
            self.grid = np.array(grid, dtype=int)
           
        # Initialisation de la matrice de récompense
        if rewards is None:
            self.rewards = np.ones((height, width), dtype=float)
        else:
            self.rewards = np.array(rewards, dtype=float)
           
        # Initialisation des points de départ et d'arrivée
        self.start = start if start is not None else (0, 0)
        self.goal = goal if goal is not None else (height - 1, width - 1)
       
    def is_in_bounds(self, row, col):
        """
        Vérifie si une cellule appartient à la grille.
       
        Args:
            row (int): Ligne de la cellule
            col (int): Colonne de la cellule
           
        Returns:
            bool: True si la cellule est dans les limites de la grille, False sinon
        """
        return 0 <= row < self.height and 0 <= col < self.width
   
    def is_passable(self, row, col):
        """
        Vérifie si une cellule est franchissable (pas un obstacle).
       
        Args:
            row (int): Ligne de la cellule
            col (int): Colonne de la cellule
           
        Returns:
            bool: True si la cellule est franchissable, False sinon
        """
        if not self.is_in_bounds(row, col):
            return False
        return self.grid[row, col] == 0
   
    def get_neighbors(self, row, col):
        """
        Identifie les cellules voisines accessibles depuis une position donnée.
        Voisinage à quatre directions : haut, bas, gauche, droite.
       
        Args:
            row (int): Ligne de la cellule courante
            col (int): Colonne de la cellule courante
           
        Returns:
            list: Liste des coordonnées (ligne, colonne) des voisins accessibles
        """
        neighbors = []
       
        # Définition des 4 directions : haut, bas, gauche, droite
        directions = [
            (-1, 0),  # Haut
            (1, 0),   # Bas
            (0, -1),  # Gauche
            (0, 1)    # Droite
        ]
       
        for d_row, d_col in directions:
            new_row = row + d_row
            new_col = col + d_col
           
            # Vérifier si le voisin est dans la grille et franchissable
            if self.is_passable(new_row, new_col):
                neighbors.append((new_row, new_col))
               
        return neighbors
   
    def get_reward(self, row, col):
        """
        Obtient la récompense associée à une cellule.
       
        Args:
            row (int): Ligne de la cellule
            col (int): Colonne de la cellule
           
        Returns:
            float: Valeur de la récompense
        """
        if self.is_in_bounds(row, col):
            return self.rewards[row, col]
        return 0.0
   
    def set_obstacle(self, row, col):
        """
        Place un obstacle à une position donnée.
       
        Args:
            row (int): Ligne de la cellule
            col (int): Colonne de la cellule
        """
        if self.is_in_bounds(row, col):
            self.grid[row, col] = 1
           
    def remove_obstacle(self, row, col):
        """
        Retire un obstacle d'une position donnée.
       
        Args:
            row (int): Ligne de la cellule
            col (int): Colonne de la cellule
        """
        if self.is_in_bounds(row, col):
            self.grid[row, col] = 0
           
    def set_reward(self, row, col, value):
        """
        Définit la récompense d'une cellule.
       
        Args:
            row (int): Ligne de la cellule
            col (int): Colonne de la cellule
            value (float): Valeur de la récompense
        """
        if self.is_in_bounds(row, col):
            self.rewards[row, col] = value
   
    def heuristic(self, row, col):
        """
        Calcule l'heuristique (distance de Manhattan) entre une cellule et l'arrivée.
       
        Args:
            row (int): Ligne de la cellule
            col (int): Colonne de la cellule
           
        Returns:
            float: Distance de Manhattan jusqu'à l'arrivée
        """
        goal_row, goal_col = self.goal
        return abs(row - goal_row) + abs(col - goal_col)
   
    def solve(self):
        """
        Résout le labyrinthe en utilisant l'algorithme A*.
        Retourne le chemin optimal du point de départ au point d'arrivée.
       
        Returns:
            list: Liste ordonnée des cellules (row, col) constituant le chemin optimal,
                  ou None si aucun chemin n'existe
        """
        # File de priorité : (priorité, compteur, (row, col))
        # priorité = coût_g + heuristique
        open_set = []
        counter = 0  # Compteur pour départager les éléments de même priorité
       
        start_row, start_col = self.start
        heapq.heappush(open_set, (self.heuristic(start_row, start_col), counter, self.start))
        counter += 1
       
        # Dictionnaire pour stocker le meilleur coût g pour atteindre chaque cellule
        g_cost = {self.start: 0}
       
        # Dictionnaire pour stocker les relations de parenté (pour reconstruire le chemin)
        came_from = {}
       
        # Ensemble des cellules déjà explorées
        closed_set = set()
       
        while open_set:
            # Récupérer la cellule avec la priorité la plus basse
            _, _, current = heapq.heappop(open_set)
           
            # Si on a atteint l'arrivée, reconstruire et retourner le chemin
            if current == self.goal:
                return self._reconstruct_path(came_from, current)
           
            # Marquer la cellule comme explorée
            if current in closed_set:
                continue
            closed_set.add(current)
           
            current_row, current_col = current
            current_g_cost = g_cost[current]
           
            # Explorer tous les voisins
            for neighbor in self.get_neighbors(current_row, current_col):
                neighbor_row, neighbor_col = neighbor
               
                # Ignorer les cellules déjà explorées
                if neighbor in closed_set:
                    continue
               
                # Calculer le coût g pour atteindre ce voisin
                # Le coût est le coût actuel moins la récompense de la cellule voisine
                # (les récompenses négatives augmentent le coût, les positives le diminuent)
                tentative_g_cost = current_g_cost - self.get_reward(neighbor_row, neighbor_col)
               
                # Si ce chemin vers le voisin est meilleur que les précédents
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    # Mémoriser ce meilleur chemin
                    came_from[neighbor] = current
                    g_cost[neighbor] = tentative_g_cost
                   
                    # Calculer la priorité f = g + h
                    f_cost = tentative_g_cost + self.heuristic(neighbor_row, neighbor_col)
                   
                    # Ajouter le voisin à la file de priorité
                    heapq.heappush(open_set, (f_cost, counter, neighbor))
                    counter += 1
       
        # Si la file est vide et qu'on n'a pas atteint l'arrivée, aucun chemin n'existe
        return None
   
    def solve_dijkstra(self):
        """
        Résout le labyrinthe en utilisant l'algorithme de Dijkstra.
        Retourne le chemin optimal du point de départ au point d'arrivée.
       
        Returns:
            list: Liste ordonnée des cellules (row, col) constituant le chemin optimal,
                  ou None si aucun chemin n'existe
        """
        # File de priorité : (distance, compteur, (row, col))
        open_set = []
        counter = 0
       
        # Distance initiale de 0 pour le départ
        heapq.heappush(open_set, (0, counter, self.start))
        counter += 1
       
        # Dictionnaire pour stocker les distances minimales
        dist = {self.start: 0}
       
        # Dictionnaire pour stocker les relations de parenté
        came_from = {}
       
        # Ensemble des cellules déjà explorées
        closed_set = set()
       
        while open_set:
            # Récupérer la cellule avec la distance minimale
            current_dist, _, current = heapq.heappop(open_set)
           
            # Si on a atteint l'arrivée, reconstruire et retourner le chemin
            if current == self.goal:
                return self._reconstruct_path(came_from, current)
           
            # Marquer la cellule comme explorée
            if current in closed_set:
                continue
            closed_set.add(current)
           
            current_row, current_col = current
           
            # Explorer tous les voisins
            for neighbor in self.get_neighbors(current_row, current_col):
                neighbor_row, neighbor_col = neighbor
               
                # Ignorer les cellules déjà explorées
                if neighbor in closed_set:
                    continue
               
                # Calculer la distance pour atteindre ce voisin
                # La distance est la distance actuelle moins la récompense de la cellule voisine
                tentative_dist = current_dist - self.get_reward(neighbor_row, neighbor_col)
               
                # Si ce chemin vers le voisin est meilleur que les précédents
                if neighbor not in dist or tentative_dist < dist[neighbor]:
                    # Mémoriser ce meilleur chemin
                    came_from[neighbor] = current
                    dist[neighbor] = tentative_dist
                   
                    # Ajouter le voisin à la file de priorité
                    heapq.heappush(open_set, (tentative_dist, counter, neighbor))
                    counter += 1
       
        # Si la file est vide et qu'on n'a pas atteint l'arrivée, aucun chemin n'existe
        return None
   
    def _reconstruct_path(self, came_from, current):
        """
        Reconstruit le chemin à partir des relations de parenté.
       
        Args:
            came_from (dict): Dictionnaire des relations de parenté
            current (tuple): Cellule d'arrivée
           
        Returns:
            list: Liste ordonnée des cellules du chemin depuis le départ jusqu'à l'arrivée
        """
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()  # Inverser pour avoir le chemin du départ vers l'arrivée
        return path
           
    def __str__(self):
        """
        Représentation textuelle du labyrinthe.
       
        Returns:
            str: Représentation du labyrinthe
        """
        result = f"Maze {self.height}x{self.width}\n"
        result += f"Start: {self.start}, Goal: {self.goal}\n"
        result += "Grid:\n"
       
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.start:
                    result += "S "
                elif (i, j) == self.goal:
                    result += "G "
                elif self.grid[i, j] == 1:
                    result += "# "
                else:
                    result += ". "
            result += "\n"
           
        return result


# Exemple d'utilisation
if __name__ == "__main__":
    # Création d'un labyrinthe de test 5x5
    maze = Maze(5, 5)
   
    # Ajout d'obstacles
    maze.set_obstacle(1, 1)
    maze.set_obstacle(1, 2)
    maze.set_obstacle(2, 2)
    maze.set_obstacle(3, 2)
   
    # Définition des points de départ et d'arrivée
    maze.start = (0, 0)
    maze.goal = (4, 4)
   
    # Initialiser les récompenses
    maze.rewards = np.full((maze.height, maze.width), -1.0)
    maze.set_reward(*maze.goal, 100.0)
   
    # Affichage du labyrinthe
    print(maze)
   
    # Test des méthodes
    print("Cellule (1, 1) est franchissable ?", maze.is_passable(1, 1))
    print("Cellule (0, 0) est franchissable ?", maze.is_passable(0, 0))
    print("Voisins de (0, 0):", maze.get_neighbors(0, 0))
    print("Voisins de (2, 1):", maze.get_neighbors(2, 1))
   
    # Test de l'algorithme A*
    print("\n=== Résolution avec A* ===")
    path = maze.solve()
    if path:
        print(f"Chemin trouvé avec {len(path)} cellules :")
        print(path)
       
        # Affichage du chemin dans la grille
        print("\nLabyrinthe avec le chemin (X) :")
        for i in range(maze.height):
            for j in range(maze.width):
                if (i, j) == maze.start:
                    print("S ", end="")
                elif (i, j) == maze.goal:
                    print("G ", end="")
                elif (i, j) in path:
                    print("X ", end="")
                elif maze.grid[i, j] == 1:
                    print("# ", end="")
                else:
                    print(". ", end="")
            print()
    else:
        print("Aucun chemin trouvé !")
   
    # Test avec un labyrinthe sans solution
    print("\n=== Test sans solution ===")
    maze2 = Maze(5, 5)
    # Créer un mur qui bloque complètement l'accès à l'arrivée
    for i in range(maze2.height):
        maze2.set_obstacle(i, 2)
    maze2.start = (0, 0)
    maze2.goal = (4, 4)
    print(maze2)
    path2 = maze2.solve()
    if path2:
        print(f"Chemin trouvé : {path2}")
    else:
        print("Aucun chemin trouvé (comme attendu !)")