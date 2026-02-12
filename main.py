import numpy as np
from Maze import Maze


def generate_random_obstacles(maze, obstacle_density=0.2, ensure_path=True):
    """
    Génère des obstacles de manière aléatoire dans le labyrinthe.
   
    Args:
        maze (Maze): Le labyrinthe à modifier
        obstacle_density (float): Densité d'obstacles (entre 0 et 1)
        ensure_path (bool): Si True, garantit que départ et arrivée restent franchissables
       
    Returns:
        Maze: Le labyrinthe modifié
    """
    for i in range(maze.height):
        for j in range(maze.width):
            # Ne jamais placer d'obstacle sur le départ ou l'arrivée
            if ensure_path and ((i, j) == maze.start or (i, j) == maze.goal):
                continue
           
            # Placer un obstacle avec une certaine probabilité
            if np.random.random() < obstacle_density:
                maze.set_obstacle(i, j)
   
    return maze


def generate_deterministic_obstacles(maze, obstacle_pattern="vertical_walls"):
    """
    Génère des obstacles de manière déterministe selon un motif.
   
    Args:
        maze (Maze): Le labyrinthe à modifier
        obstacle_pattern (str): Type de motif ("vertical_walls", "horizontal_walls", "maze_pattern")
       
    Returns:
        Maze: Le labyrinthe modifié
    """
    if obstacle_pattern == "vertical_walls":
        # Murs verticaux avec des ouvertures
        for col in range(2, maze.width, 4):
            for row in range(maze.height):
                if (row, col) != maze.start and (row, col) != maze.goal:
                    # Laisser des ouvertures tous les 3 rangées
                    if row % 3 != 0:
                        maze.set_obstacle(row, col)
                       
    elif obstacle_pattern == "horizontal_walls":
        # Murs horizontaux avec des ouvertures
        for row in range(2, maze.height, 4):
            for col in range(maze.width):
                if (row, col) != maze.start and (row, col) != maze.goal:
                    # Laisser des ouvertures toutes les 3 colonnes
                    if col % 3 != 0:
                        maze.set_obstacle(row, col)
                       
    elif obstacle_pattern == "maze_pattern":
        # Motif de labyrinthe plus complexe
        for i in range(1, maze.height - 1, 2):
            for j in range(1, maze.width - 1, 2):
                if (i, j) != maze.start and (i, j) != maze.goal:
                    maze.set_obstacle(i, j)
                    # Étendre l'obstacle dans une direction aléatoire
                    direction = np.random.choice(['up', 'down', 'left', 'right'])
                    if direction == 'up' and i > 0:
                        maze.set_obstacle(i - 1, j)
                    elif direction == 'down' and i < maze.height - 1:
                        maze.set_obstacle(i + 1, j)
                    elif direction == 'left' and j > 0:
                        maze.set_obstacle(i, j - 1)
                    elif direction == 'right' and j < maze.width - 1:
                        maze.set_obstacle(i, j + 1)
   
    return maze


def initialize_uniform_rewards(maze, step_cost=-1.0, goal_reward=100.0):
    """
    Initialise la matrice de récompense de manière cohérente.
    Applique une pénalité uniforme à chaque déplacement pour encourager les chemins courts.
   
    Args:
        maze (Maze): Le labyrinthe à modifier
        step_cost (float): Coût de chaque déplacement (valeur négative pour pénaliser)
        goal_reward (float): Récompense significative pour la cellule d'arrivée
       
    Returns:
        Maze: Le labyrinthe modifié
    """
    # Initialiser toutes les cellules avec le coût de déplacement
    maze.rewards = np.full((maze.height, maze.width), step_cost, dtype=float)
   
    # Définir une récompense significative pour la cellule d'arrivée
    goal_row, goal_col = maze.goal
    maze.rewards[goal_row, goal_col] = goal_reward
   
    return maze


def add_bonus_cells(maze, num_bonuses=5, bonus_value=10.0, random_placement=True,
                    bonus_positions=None):
    """
    Ajoute des bonus sur certaines cellules du labyrinthe.
   
    Args:
        maze (Maze): Le labyrinthe à modifier
        num_bonuses (int): Nombre de bonus à ajouter (si random_placement=True)
        bonus_value (float): Valeur du bonus
        random_placement (bool): Si True, place les bonus aléatoirement
        bonus_positions (list): Liste de positions (row, col) pour les bonus (si random_placement=False)
       
    Returns:
        Maze: Le labyrinthe modifié
    """
    if random_placement:
        # Placer des bonus de manière aléatoire
        bonuses_placed = 0
        attempts = 0
        max_attempts = num_bonuses * 10  # Éviter une boucle infinie
       
        while bonuses_placed < num_bonuses and attempts < max_attempts:
            row = np.random.randint(0, maze.height)
            col = np.random.randint(0, maze.width)
           
            # Vérifier que la cellule est franchissable et n'est pas départ/arrivée
            if (maze.is_passable(row, col) and
                (row, col) != maze.start and
                (row, col) != maze.goal):
                maze.set_reward(row, col, bonus_value)
                bonuses_placed += 1
           
            attempts += 1
    else:
        # Placer des bonus aux positions spécifiées
        if bonus_positions is not None:
            for row, col in bonus_positions:
                if (maze.is_passable(row, col) and
                    (row, col) != maze.start and
                    (row, col) != maze.goal):
                    maze.set_reward(row, col, bonus_value)
   
    return maze


def generate_movable_areas(maze, movable_ratio=0.7):
    """
    Génère les zones franchissables en définissant le ratio de cellules libres.
   
    Args:
        maze (Maze): Le labyrinthe à modifier
        movable_ratio (float): Ratio de cellules franchissables (entre 0 et 1)
       
    Returns:
        Maze: Le labyrinthe modifié
    """
    obstacle_density = 1.0 - movable_ratio
    return generate_random_obstacles(maze, obstacle_density=obstacle_density, ensure_path=True)


def create_complete_maze(width, height, start=None, goal=None,
                        obstacle_type="random", obstacle_density=0.2,
                        step_cost=-1.0, goal_reward=100.0,
                        add_bonuses=True, num_bonuses=5, bonus_value=10.0):
    """
    Crée un labyrinthe complet avec obstacles et récompenses.
   
    Args:
        width (int): Largeur du labyrinthe
        height (int): Hauteur du labyrinthe
        start (tuple): Position de départ (row, col)
        goal (tuple): Position d'arrivée (row, col)
        obstacle_type (str): Type d'obstacles ("random", "vertical_walls", "horizontal_walls", "maze_pattern")
        obstacle_density (float): Densité d'obstacles pour le type "random"
        step_cost (float): Coût de chaque déplacement
        goal_reward (float): Récompense pour l'arrivée
        add_bonuses (bool): Ajouter des bonus
        num_bonuses (int): Nombre de bonus
        bonus_value (float): Valeur des bonus
       
    Returns:
        Maze: Le labyrinthe généré
    """
    # Définir les positions par défaut
    if start is None:
        start = (0, 0)
    if goal is None:
        goal = (height - 1, width - 1)
   
    # Créer le labyrinthe de base
    maze = Maze(width, height, start=start, goal=goal)
   
    # Générer les obstacles
    if obstacle_type == "random":
        generate_random_obstacles(maze, obstacle_density=obstacle_density)
    else:
        generate_deterministic_obstacles(maze, obstacle_pattern=obstacle_type)
   
    # S'assurer que départ et arrivée sont franchissables
    maze.remove_obstacle(*start)
    maze.remove_obstacle(*goal)
   
    # Initialiser les récompenses
    initialize_uniform_rewards(maze, step_cost=step_cost, goal_reward=goal_reward)
   
    # Ajouter des bonus
    if add_bonuses:
        add_bonus_cells(maze, num_bonuses=num_bonuses, bonus_value=bonus_value)
   
    return maze


# Exemples d'utilisation
if __name__ == "__main__":
    print("=== Exemple 1 : Labyrinthe avec obstacles aléatoires ===")
    maze1 = create_complete_maze(10, 10, obstacle_type="random", obstacle_density=0.2)
    print(maze1)
    print(f"Récompense à l'arrivée : {maze1.get_reward(*maze1.goal)}")
   
    print("\n=== Exemple 2 : Labyrinthe avec murs verticaux ===")
    maze2 = create_complete_maze(12, 8, obstacle_type="vertical_walls")
    print(maze2)
   
    print("\n=== Exemple 3 : Labyrinthe avec murs horizontaux ===")
    maze3 = create_complete_maze(10, 10, obstacle_type="horizontal_walls")
    print(maze3)
   
    print("\n=== Exemple 4 : Labyrinthe avec motif complexe ===")
    maze4 = create_complete_maze(15, 15, obstacle_type="maze_pattern",
                                 add_bonuses=True, num_bonuses=8, bonus_value=15.0)
    print(maze4)
    print(f"Voisins de la position de départ {maze4.start}: {maze4.get_neighbors(*maze4.start)}")