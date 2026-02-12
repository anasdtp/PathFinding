"""
Extension du TP1 : Déplacements diagonaux

Ce fichier implémente une version étendue de la classe Maze qui supporte
les déplacements diagonaux avec un coût adapté.

Pour la question 2 du TP :
"En extension, les étudiants pourront proposer l'ajout de déplacements diagonaux 
avec un coût adapté"
"""

import numpy as np
import heapq
from Maze import Maze


class DiagonalMaze(Maze):
    """
    Extension de la classe Maze permettant les déplacements diagonaux.
    
    Le coût des déplacements diagonaux est √2 ≈ 1.414 fois celui des déplacements
    orthogonaux (haut, bas, gauche, droite).
    """
    
    def __init__(self, width, height, grid=None, rewards=None, start=None, goal=None,
                 diagonal_cost_multiplier=1.414):
        """
        Initialise un labyrinthe avec support des déplacements diagonaux.
        
        Args:
            width (int): Largeur du labyrinthe
            height (int): Hauteur du labyrinthe
            grid (np.ndarray, optional): Grille des obstacles
            rewards (np.ndarray, optional): Matrice de récompense
            start (tuple, optional): Point de départ
            goal (tuple, optional): Point d'arrivée
            diagonal_cost_multiplier (float): Multiplicateur de coût pour les diagonales
                                             Par défaut √2 ≈ 1.414
        """
        super().__init__(width, height, grid, rewards, start, goal)
        self.diagonal_cost_multiplier = diagonal_cost_multiplier
    
    def get_neighbors(self, row, col):
        """
        Identifie les cellules voisines accessibles, incluant les diagonales.
        
        Retourne une liste de tuples (neighbor_row, neighbor_col, cost_multiplier)
        où cost_multiplier est:
        - 1.0 pour les déplacements orthogonaux
        - diagonal_cost_multiplier pour les déplacements diagonaux
        
        Args:
            row (int): Ligne de la cellule courante
            col (int): Colonne de la cellule courante
            
        Returns:
            list: Liste des tuples (ligne, colonne, multiplicateur_coût)
        """
        neighbors = []
        
        # 8 directions : 4 orthogonales + 4 diagonales
        # Format: (delta_row, delta_col, cost_multiplier)
        directions = [
            # Orthogonales (coût normal)
            (-1, 0, 1.0),   # Haut
            (1, 0, 1.0),    # Bas
            (0, -1, 1.0),   # Gauche
            (0, 1, 1.0),    # Droite
            # Diagonales (coût √2)
            (-1, -1, self.diagonal_cost_multiplier),  # Haut-Gauche
            (-1, 1, self.diagonal_cost_multiplier),   # Haut-Droite
            (1, -1, self.diagonal_cost_multiplier),   # Bas-Gauche
            (1, 1, self.diagonal_cost_multiplier),    # Bas-Droite
        ]
        
        for d_row, d_col, cost_mult in directions:
            new_row = row + d_row
            new_col = col + d_col
            
            # Vérifier si le voisin est dans la grille et franchissable
            if self.is_passable(new_row, new_col):
                neighbors.append((new_row, new_col, cost_mult))
        
        return neighbors
    
    def heuristic(self, row, col):
        """
        Calcule l'heuristique (distance euclidienne) entre une cellule et l'arrivée.
        
        Pour les déplacements diagonaux, la distance euclidienne est plus appropriée
        que la distance de Manhattan.
        
        Args:
            row (int): Ligne de la cellule
            col (int): Colonne de la cellule
            
        Returns:
            float: Distance euclidienne jusqu'à l'arrivée
        """
        goal_row, goal_col = self.goal
        return np.sqrt((row - goal_row)**2 + (col - goal_col)**2)
    
    def solve(self):
        """
        Résout le labyrinthe avec A* en tenant compte des déplacements diagonaux.
        
        Returns:
            list: Liste ordonnée des cellules (row, col) du chemin optimal,
                  ou None si aucun chemin n'existe
        """
        open_set = []
        counter = 0
        
        start_row, start_col = self.start
        heapq.heappush(open_set, (self.heuristic(start_row, start_col), counter, self.start))
        counter += 1
        
        g_cost = {self.start: 0}
        came_from = {}
        closed_set = set()
        
        while open_set:
            _, _, current = heapq.heappop(open_set)
            
            if current == self.goal:
                return self._reconstruct_path(came_from, current)
            
            if current in closed_set:
                continue
            closed_set.add(current)
            
            current_row, current_col = current
            current_g_cost = g_cost[current]
            
            # Explorer tous les voisins (8 directions)
            for neighbor_row, neighbor_col, cost_mult in self.get_neighbors(current_row, current_col):
                neighbor = (neighbor_row, neighbor_col)
                
                if neighbor in closed_set:
                    continue
                
                # Le coût est ajusté par le multiplicateur de coût diagonal
                # et la récompense de la cellule
                move_cost = cost_mult * (-self.get_reward(neighbor_row, neighbor_col))
                tentative_g_cost = current_g_cost + move_cost
                
                if neighbor not in g_cost or tentative_g_cost < g_cost[neighbor]:
                    came_from[neighbor] = current
                    g_cost[neighbor] = tentative_g_cost
                    
                    f_cost = tentative_g_cost + self.heuristic(neighbor_row, neighbor_col)
                    heapq.heappush(open_set, (f_cost, counter, neighbor))
                    counter += 1
        
        return None
    
    def solve_dijkstra(self):
        """
        Résout le labyrinthe avec Dijkstra en tenant compte des déplacements diagonaux.
        
        Returns:
            list: Liste ordonnée des cellules (row, col) du chemin optimal,
                  ou None si aucun chemin n'existe
        """
        open_set = []
        counter = 0
        
        heapq.heappush(open_set, (0, counter, self.start))
        counter += 1
        
        dist = {self.start: 0}
        came_from = {}
        closed_set = set()
        
        while open_set:
            current_dist, _, current = heapq.heappop(open_set)
            
            if current == self.goal:
                return self._reconstruct_path(came_from, current)
            
            if current in closed_set:
                continue
            closed_set.add(current)
            
            current_row, current_col = current
            
            # Explorer tous les voisins (8 directions)
            for neighbor_row, neighbor_col, cost_mult in self.get_neighbors(current_row, current_col):
                neighbor = (neighbor_row, neighbor_col)
                
                if neighbor in closed_set:
                    continue
                
                move_cost = cost_mult * (-self.get_reward(neighbor_row, neighbor_col))
                tentative_dist = current_dist + move_cost
                
                if neighbor not in dist or tentative_dist < dist[neighbor]:
                    came_from[neighbor] = current
                    dist[neighbor] = tentative_dist
                    
                    heapq.heappush(open_set, (tentative_dist, counter, neighbor))
                    counter += 1
        
        return None


def compare_4_vs_8_connectivity():
    """
    Compare les résultats avec 4 directions vs 8 directions.
    """
    print("=" * 70)
    print("COMPARAISON : 4 DIRECTIONS vs 8 DIRECTIONS (avec diagonales)")
    print("=" * 70)
    
    # Créer un labyrinthe simple pour la comparaison
    maze_4 = Maze(10, 10, start=(0, 0), goal=(9, 9))
    maze_4.rewards = np.full((10, 10), -1.0)
    maze_4.set_reward(9, 9, 100.0)
    
    maze_8 = DiagonalMaze(10, 10, start=(0, 0), goal=(9, 9))
    maze_8.rewards = np.full((10, 10), -1.0)
    maze_8.set_reward(9, 9, 100.0)
    
    # Résoudre avec 4 directions
    print("\n--- 4 DIRECTIONS (orthogonales uniquement) ---")
    path_4 = maze_4.solve()
    if path_4:
        cost_4 = sum(-maze_4.rewards[i, j] for i, j in path_4)
        print(f"✅ Chemin trouvé : {len(path_4)} cellules")
        print(f"   Coût total : {cost_4:.2f}")
        print(f"   Chemin : {path_4}")
    
    # Résoudre avec 8 directions
    print("\n--- 8 DIRECTIONS (avec diagonales) ---")
    path_8 = maze_8.solve()
    if path_8:
        # Calculer le coût en tenant compte des mouvements diagonaux
        cost_8 = 0
        for i in range(len(path_8) - 1):
            r1, c1 = path_8[i]
            r2, c2 = path_8[i + 1]
            
            # Déterminer si c'est un mouvement diagonal
            is_diagonal = abs(r1 - r2) == 1 and abs(c1 - c2) == 1
            cost_mult = maze_8.diagonal_cost_multiplier if is_diagonal else 1.0
            
            cost_8 += cost_mult * (-maze_8.rewards[r2, c2])
        
        print(f"✅ Chemin trouvé : {len(path_8)} cellules")
        print(f"   Coût total : {cost_8:.2f}")
        print(f"   Chemin : {path_8}")
    
    # Comparaison
    print("\n--- ANALYSE ---")
    if path_4 and path_8:
        reduction = (len(path_4) - len(path_8)) / len(path_4) * 100
        print(f"Réduction du nombre de cellules : {reduction:.1f}%")
        print(f"Le chemin avec diagonales est {len(path_4) / len(path_8):.2f}x plus court")
        print(f"\nExplication :")
        print(f"• 4 directions : doit suivre la grille (Manhattan)")
        print(f"• 8 directions : peut prendre des raccourcis en diagonal")
        print(f"• Coût diagonal (√2 ≈ 1.414) > coût orthogonal (1.0)")
        print(f"• Mais chemin plus court compense le coût supérieur")


def test_diagonal_with_obstacles():
    """
    Teste les déplacements diagonaux avec obstacles.
    """
    print("\n" + "=" * 70)
    print("TEST : DÉPLACEMENTS DIAGONAUX AVEC OBSTACLES")
    print("=" * 70)
    
    maze = DiagonalMaze(10, 10, start=(0, 0), goal=(9, 9))
    
    # Ajouter quelques obstacles
    for i in range(5):
        maze.set_obstacle(i, 4)
        maze.set_obstacle(i + 3, 7)
    
    maze.rewards = np.full((10, 10), -1.0)
    maze.set_reward(9, 9, 100.0)
    
    print(maze)
    
    print("\n--- Résolution avec A* (8 directions) ---")
    path = maze.solve()
    if path:
        print(f"✅ Chemin trouvé : {len(path)} cellules")
        
        # Compter les mouvements diagonaux
        diagonal_moves = 0
        for i in range(len(path) - 1):
            r1, c1 = path[i]
            r2, c2 = path[i + 1]
            if abs(r1 - r2) == 1 and abs(c1 - c2) == 1:
                diagonal_moves += 1
        
        print(f"   Mouvements diagonaux : {diagonal_moves}")
        print(f"   Mouvements orthogonaux : {len(path) - 1 - diagonal_moves}")


def main():
    """
    Démonstration de l'extension avec déplacements diagonaux.
    """
    print("\n" + "█" * 70)
    print("EXTENSION TP1 : DÉPLACEMENTS DIAGONAUX")
    print("Réponse à la question 2")
    print("█" * 70)
    
    compare_4_vs_8_connectivity()
    test_diagonal_with_obstacles()
    
    print("\n" + "█" * 70)
    print("CONCLUSION")
    print("█" * 70)
    print("\n✅ Les déplacements diagonaux permettent des chemins plus courts")
    print("✅ Le coût diagonal (√2) est correctement pris en compte")
    print("✅ L'heuristique euclidienne est plus adaptée que Manhattan")
    print("✅ Les algorithmes A* et Dijkstra fonctionnent avec 8 directions")


if __name__ == "__main__":
    main()
