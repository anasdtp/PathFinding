"""
TP2 - Recherche Bidirectionnelle avec Dijkstra et A*
Implémentation de la recherche bidirectionnelle pour optimiser la recherche de chemin
"""

import heapq
import numpy as np
import time


class BiDirectionalMaze:
    """
    Classe pour résoudre des labyrinthes avec recherche bidirectionnelle.
    Supporte Dijkstra bidirectionnel et A* bidirectionnel.
    """
    
    def __init__(self, width, height, grid=None, rewards=None, start=None, goal=None):
        """
        Initialise le labyrinthe.
        
        Args:
            width: Largeur du labyrinthe
            height: Hauteur du labyrinthe
            grid: Matrice d'obstacles (0=libre, 1=obstacle)
            rewards: Matrice de récompenses
            start: Position de départ (row, col)
            goal: Position d'arrivée (row, col)
        """
        self.width = width
        self.height = height
        self.grid = np.zeros((height, width), dtype=int) if grid is None else np.array(grid, dtype=int)
        self.rewards = np.ones((height, width), dtype=float) if rewards is None else np.array(rewards, dtype=float)
        self.start = start if start is not None else (0, 0)
        self.goal = goal if goal is not None else (height - 1, width - 1)
        
    def is_in_bounds(self, row, col):
        """Vérifie si une cellule est dans la grille."""
        return 0 <= row < self.height and 0 <= col < self.width
    
    def is_passable(self, row, col):
        """Vérifie si une cellule est franchissable."""
        return self.is_in_bounds(row, col) and self.grid[row, col] == 0
    
    def get_neighbors(self, row, col):
        """Retourne les voisins 4-connexes franchissables."""
        neighbors = []
        for dr, dc in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nr, nc = row + dr, col + dc
            if self.is_passable(nr, nc):
                neighbors.append((nr, nc))
        return neighbors
    
    def heuristic(self, row, col, goal=None):
        """Distance de Manhattan vers le but."""
        if goal is None:
            goal = self.goal
        return abs(goal[0] - row) + abs(goal[1] - col)

    def _safe_reconstruct(self, came_from, start_node, reverse=False):
        """Reconstruit un chemin parent->enfant avec garde anti-boucle."""
        path = [start_node]
        current = start_node
        seen = {start_node}
        max_steps = self.width * self.height + 1

        for _ in range(max_steps):
            if current not in came_from:
                break
            current = came_from[current]
            if current in seen:
                # Garde anti-boucle : on arrête la reconstruction si un cycle apparaît.
                break
            seen.add(current)
            path.append(current)

        if reverse:
            path.reverse()
        return path
    
    def dijkstra_bidirectional(self, return_explored=False, return_sets=False):
        """
        Algorithme Dijkstra bidirectionnel.
        Recherche depuis le départ ET depuis le but simultanément.
        
                Returns:
                        - return_explored=False: path ou None
                        - return_explored=True: (path, cost, elapsed, explored_count)
                        - return_explored=True et return_sets=True:
                            (path, cost, elapsed, explored_count, closed_forward, closed_backward)
        """
        start_time = time.time()
        
        # Files de priorité pour chaque direction
        open_forward = []
        open_backward = []
        
        counter = [0, 0]  # Compteurs pour éviter les ties
        
        # Initialisation avant (départ → but)
        heapq.heappush(open_forward, (0, counter[0], self.start))
        counter[0] += 1
        
        # Initialisation arrière (but → départ)
        heapq.heappush(open_backward, (0, counter[1], self.goal))
        counter[1] += 1
        
        # Dictionnaires pour stocker les coûts et chemins
        g_forward = {self.start: 0}
        g_backward = {self.goal: 0}
        
        came_from_forward = {}
        came_from_backward = {}
        
        closed_forward = set()
        closed_backward = set()
        
        # Conditions de convergence
        best_cost = float('inf')
        meeting_point_forward = None
        meeting_point_backward = None
        
        while open_forward or open_backward:
            # Étape avant
            if open_forward:
                f_cost, _, current_f = heapq.heappop(open_forward)
                
                if current_f in closed_forward:
                    continue
                
                closed_forward.add(current_f)
                
                # Vérifier si on rencontre la recherche arrière
                if current_f in closed_backward:
                    # Chemin trouvé
                    cost = g_forward[current_f] + g_backward[current_f]
                    if cost < best_cost:
                        best_cost = cost
                        meeting_point_forward = current_f
                        meeting_point_backward = current_f
                
                # Explorer les voisins
                for neighbor in self.get_neighbors(current_f[0], current_f[1]):
                    new_cost = g_forward[current_f] - self.rewards[neighbor[0], neighbor[1]]
                    
                    if neighbor not in g_forward or new_cost < g_forward[neighbor]:
                        g_forward[neighbor] = new_cost
                        came_from_forward[neighbor] = current_f
                        heapq.heappush(open_forward, (new_cost, counter[0], neighbor))
                        counter[0] += 1
                        
                        # Vérifier convergence
                        if neighbor in closed_backward:
                            cost = new_cost + g_backward[neighbor]
                            if cost < best_cost:
                                best_cost = cost
                                meeting_point_forward = neighbor
                                meeting_point_backward = neighbor
            
            # Étape arrière
            if open_backward:
                f_cost, _, current_b = heapq.heappop(open_backward)
                
                if current_b in closed_backward:
                    continue
                
                closed_backward.add(current_b)
                
                # Vérifier si on rencontre la recherche avant
                if current_b in closed_forward:
                    cost = g_forward[current_b] + g_backward[current_b]
                    if cost < best_cost:
                        best_cost = cost
                        meeting_point_forward = current_b
                        meeting_point_backward = current_b
                
                # Explorer les voisins
                for neighbor in self.get_neighbors(current_b[0], current_b[1]):
                    new_cost = g_backward[current_b] - self.rewards[neighbor[0], neighbor[1]]
                    
                    if neighbor not in g_backward or new_cost < g_backward[neighbor]:
                        g_backward[neighbor] = new_cost
                        came_from_backward[neighbor] = current_b
                        heapq.heappush(open_backward, (new_cost, counter[1], neighbor))
                        counter[1] += 1
                        
                        # Vérifier convergence
                        if neighbor in closed_forward:
                            cost = g_forward[neighbor] + new_cost
                            if cost < best_cost:
                                best_cost = cost
                                meeting_point_forward = neighbor
                                meeting_point_backward = neighbor
            
            # Critère d'arrêt : si les deux frontières ne peuvent pas s'améliorer
            if open_forward and open_backward:
                if open_forward[0][0] + open_backward[0][0] >= best_cost:
                    break
        
        elapsed = time.time() - start_time
        
        # Reconstruction du chemin
        if meeting_point_forward is None or best_cost == float('inf'):
            if not return_explored:
                return None
            explored = len(closed_forward) + len(closed_backward)
            if return_sets:
                return (None, 0, elapsed, explored, closed_forward, closed_backward)
            return (None, 0, elapsed, explored)
        
        # Chemin avant: start -> meeting
        path_forward = self._safe_reconstruct(came_from_forward, meeting_point_forward, reverse=True)

        # Chemin arrière: meeting -> goal
        path_backward = self._safe_reconstruct(came_from_backward, meeting_point_backward, reverse=False)

        # Combiner sans dupliquer le sommet de rencontre.
        path = path_forward + path_backward[1:]
        
        if return_explored:
            explored = len(closed_forward) + len(closed_backward)
            if return_sets:
                return (path, best_cost, elapsed, explored, closed_forward, closed_backward)
            return (path, best_cost, elapsed, explored)
        return path
    
    def astar_bidirectional(self, return_explored=False, return_sets=False):
        """
        Algorithme A* bidirectionnel.
        Utilise l'heuristique pour guider les deux recherches.
        
                Returns:
                        - return_explored=False: path ou None
                        - return_explored=True: (path, cost, elapsed, explored_count)
                        - return_explored=True et return_sets=True:
                            (path, cost, elapsed, explored_count, closed_forward, closed_backward)
        """
        start_time = time.time()
        
        # Files de priorité
        open_forward = []
        open_backward = []
        
        counter = [0, 0]
        
        # Initialisation avant
        h_forward = self.heuristic(self.start[0], self.start[1], self.goal)
        heapq.heappush(open_forward, (h_forward, counter[0], self.start))
        counter[0] += 1
        
        # Initialisation arrière
        h_backward = self.heuristic(self.goal[0], self.goal[1], self.start)
        heapq.heappush(open_backward, (h_backward, counter[1], self.goal))
        counter[1] += 1
        
        # Dictionnaires
        g_forward = {self.start: 0}
        g_backward = {self.goal: 0}
        
        came_from_forward = {}
        came_from_backward = {}
        
        closed_forward = set()
        closed_backward = set()
        
        # Conditions de convergence
        best_cost = float('inf')
        meeting_point_forward = None
        meeting_point_backward = None
        
        while open_forward or open_backward:
            # Étape avant
            if open_forward:
                f_cost, _, current_f = heapq.heappop(open_forward)
                
                if current_f in closed_forward:
                    continue
                
                closed_forward.add(current_f)
                
                # Vérifier rencontre
                if current_f in closed_backward:
                    cost = g_forward[current_f] + g_backward[current_f]
                    if cost < best_cost:
                        best_cost = cost
                        meeting_point_forward = current_f
                        meeting_point_backward = current_f
                
                # Explorer voisins
                for neighbor in self.get_neighbors(current_f[0], current_f[1]):
                    new_cost = g_forward[current_f] - self.rewards[neighbor[0], neighbor[1]]
                    
                    if neighbor not in g_forward or new_cost < g_forward[neighbor]:
                        g_forward[neighbor] = new_cost
                        came_from_forward[neighbor] = current_f
                        h = self.heuristic(neighbor[0], neighbor[1], self.goal)
                        f = new_cost + h
                        heapq.heappush(open_forward, (f, counter[0], neighbor))
                        counter[0] += 1
                        
                        # Vérifier convergence
                        if neighbor in closed_backward:
                            cost = new_cost + g_backward[neighbor]
                            if cost < best_cost:
                                best_cost = cost
                                meeting_point_forward = neighbor
                                meeting_point_backward = neighbor
            
            # Étape arrière
            if open_backward:
                f_cost, _, current_b = heapq.heappop(open_backward)
                
                if current_b in closed_backward:
                    continue
                
                closed_backward.add(current_b)
                
                # Vérifier rencontre
                if current_b in closed_forward:
                    cost = g_forward[current_b] + g_backward[current_b]
                    if cost < best_cost:
                        best_cost = cost
                        meeting_point_forward = current_b
                        meeting_point_backward = current_b
                
                # Explorer voisins
                for neighbor in self.get_neighbors(current_b[0], current_b[1]):
                    new_cost = g_backward[current_b] - self.rewards[neighbor[0], neighbor[1]]
                    
                    if neighbor not in g_backward or new_cost < g_backward[neighbor]:
                        g_backward[neighbor] = new_cost
                        came_from_backward[neighbor] = current_b
                        h = self.heuristic(neighbor[0], neighbor[1], self.start)
                        f = new_cost + h
                        heapq.heappush(open_backward, (f, counter[1], neighbor))
                        counter[1] += 1
                        
                        # Vérifier convergence
                        if neighbor in closed_forward:
                            cost = g_forward[neighbor] + new_cost
                            if cost < best_cost:
                                best_cost = cost
                                meeting_point_forward = neighbor
                                meeting_point_backward = neighbor
            
            # Critère d'arrêt
            if open_forward and open_backward:
                min_f_forward = open_forward[0][0]
                min_f_backward = open_backward[0][0]
                if min_f_forward + min_f_backward >= best_cost:
                    break
        
        elapsed = time.time() - start_time
        
        # Reconstruction du chemin
        if meeting_point_forward is None or best_cost == float('inf'):
            if not return_explored:
                return None
            explored = len(closed_forward) + len(closed_backward)
            if return_sets:
                return (None, 0, elapsed, explored, closed_forward, closed_backward)
            return (None, 0, elapsed, explored)
        
        # Chemin avant: start -> meeting
        path_forward = self._safe_reconstruct(came_from_forward, meeting_point_forward, reverse=True)

        # Chemin arrière: meeting -> goal
        path_backward = self._safe_reconstruct(came_from_backward, meeting_point_backward, reverse=False)

        # Combiner sans dupliquer le sommet de rencontre.
        path = path_forward + path_backward[1:]
        
        if return_explored:
            explored = len(closed_forward) + len(closed_backward)
            if return_sets:
                return (path, best_cost, elapsed, explored, closed_forward, closed_backward)
            return (path, best_cost, elapsed, explored)
        return path
