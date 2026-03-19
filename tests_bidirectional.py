"""
Tests du TP2 - Comparaison Dijkstra/A* Bidirectional vs Unidirectional
"""

import sys

from bidirectional import BiDirectionalMaze
from main import create_complete_maze


def create_tp2_maze(width, height, obstacle_type="random", obstacle_density=0.2):
    """Crée un labyrinthe TP2 sans bonus et avec coût uniforme pour comparer les algorithmes."""
    return create_complete_maze(
        width,
        height,
        obstacle_type=obstacle_type,
        obstacle_density=obstacle_density,
        step_cost=-1.0,
        goal_reward=-1.0,
        add_bonuses=False,
    )


def test_comparison():
    """Compare les algorithmes unidirectionnels et bidirectionnels."""
    
    print("\n" + "="*80)
    print("TEST 1 : Labyrinthe 10x10 sans obstacle")
    print("="*80)
    
    maze_uni = create_tp2_maze(10, 10, obstacle_type="random", obstacle_density=0.0)
    maze_bi_di = BiDirectionalMaze(10, 10, grid=maze_uni.grid, rewards=maze_uni.rewards, 
                                    start=maze_uni.start, goal=maze_uni.goal)
    maze_bi_a = BiDirectionalMaze(10, 10, grid=maze_uni.grid, rewards=maze_uni.rewards, 
                                   start=maze_uni.start, goal=maze_uni.goal)
    
    # Unidirectional Dijkstra
    path_uni_di = maze_uni.solve_dijkstra(return_explored=True)
    print(f"\nUnidirectional Dijkstra :")
    print(f"  Chemin trouvé : {len(path_uni_di[0]) if path_uni_di[0] else None} cellules")
    # print(f"  Coût : {path_uni_di[1]:.2f}")
    # print(f"  Cellules explorées : {path_uni_di[2]}")
    
    # Unidirectional A*
    path_uni_a = maze_uni.solve(return_explored=True)
    print(f"\nUnidirectional A* :")
    print(f"  Chemin trouvé : {len(path_uni_a[0]) if path_uni_a[0] else None} cellules")
    # print(f"  Coût : {path_uni_a[1]:.2f}")
    # print(f"  Cellules explorées : {path_uni_a[2]}")
    
    # Bidirectional Dijkstra
    path_bi_di = maze_bi_di.dijkstra_bidirectional(return_explored=True)
    print(f"\nBidirectional Dijkstra :")
    print(f"  Chemin trouvé : {len(path_bi_di[0]) if path_bi_di[0] else None} cellules")
    print(f"  Coût : {path_bi_di[1]:.2f}")
    print(f"  Temps : {path_bi_di[2]*1000:.2f} ms")
    print(f"  Cellules explorées : {path_bi_di[3]}")
    explored_uni_di = len(path_uni_di[1])
    if explored_uni_di > 0:
        print(f"  Réduction : {(1 - path_bi_di[3]/explored_uni_di)*100:.1f}%")
    
    # Bidirectional A*
    path_bi_a = maze_bi_a.astar_bidirectional(return_explored=True)
    print(f"\nBidirectional A* :")
    print(f"  Chemin trouvé : {len(path_bi_a[0]) if path_bi_a[0] else None} cellules")
    print(f"  Coût : {path_bi_a[1]:.2f}")
    print(f"  Temps : {path_bi_a[2]*1000:.2f} ms")
    print(f"  Cellules explorées : {path_bi_a[3]}")
    explored_uni_a = len(path_uni_a[1])
    if explored_uni_a > 0:
        print(f"  Réduction : {(1 - path_bi_a[3]/explored_uni_a)*100:.1f}%")
    
    print("\n" + "="*80)
    print("TEST 2 : Labyrinthe 10x10 avec obstacles (densité 0.2)")
    print("="*80)
    
    maze_uni = create_tp2_maze(10, 10, obstacle_type="random", obstacle_density=0.2)
    maze_bi_di = BiDirectionalMaze(10, 10, grid=maze_uni.grid, rewards=maze_uni.rewards,
                                    start=maze_uni.start, goal=maze_uni.goal)
    maze_bi_a = BiDirectionalMaze(10, 10, grid=maze_uni.grid, rewards=maze_uni.rewards,
                                   start=maze_uni.start, goal=maze_uni.goal)
    
    path_uni_di = maze_uni.solve_dijkstra(return_explored=True)
    path_uni_a = maze_uni.solve(return_explored=True)
    path_bi_di = maze_bi_di.dijkstra_bidirectional(return_explored=True)
    path_bi_a = maze_bi_a.astar_bidirectional(return_explored=True)
    
    explored_uni_di = len(path_uni_di[1])
    explored_uni_a = len(path_uni_a[1])
    print(f"\nUnidirectional Dijkstra : {explored_uni_di} cellules explorées")
    print(f"Unidirectional A* : {explored_uni_a} cellules explorées")
    print(f"Bidirectional Dijkstra : {path_bi_di[3]} cellules explorées ({(1 - path_bi_di[3]/explored_uni_di)*100:.1f}% réduction)")
    print(f"Bidirectional A* : {path_bi_a[3]} cellules explorées ({(1 - path_bi_a[3]/explored_uni_a)*100:.1f}% réduction)")
    
    print("\n" + "="*80)
    print("TEST 3 : Labyrinthe 12x8 avec murs verticaux")
    print("="*80)
    
    maze_uni = create_tp2_maze(12, 8, obstacle_type="vertical_walls")
    maze_bi_di = BiDirectionalMaze(12, 8, grid=maze_uni.grid, rewards=maze_uni.rewards,
                                    start=maze_uni.start, goal=maze_uni.goal)
    maze_bi_a = BiDirectionalMaze(12, 8, grid=maze_uni.grid, rewards=maze_uni.rewards,
                                   start=maze_uni.start, goal=maze_uni.goal)
    
    path_uni_di = maze_uni.solve_dijkstra(return_explored=True)
    path_uni_a = maze_uni.solve(return_explored=True)
    path_bi_di = maze_bi_di.dijkstra_bidirectional(return_explored=True)
    path_bi_a = maze_bi_a.astar_bidirectional(return_explored=True)
    
    explored_uni_di = len(path_uni_di[1])
    explored_uni_a = len(path_uni_a[1])
    print(f"\nUnidirectional Dijkstra : {explored_uni_di} cellules explorées")
    print(f"Unidirectional A* : {explored_uni_a} cellules explorées")
    print(f"Bidirectional Dijkstra : {path_bi_di[3]} cellules explorées ({(1 - path_bi_di[3]/explored_uni_di)*100:.1f}% réduction)")
    print(f"Bidirectional A* : {path_bi_a[3]} cellules explorées ({(1 - path_bi_a[3]/explored_uni_a)*100:.1f}% réduction)")
    
    print("\n" + "="*80)
    print("TEST 4 : Grand labyrinthe 30x30 motif maze_pattern")
    print("="*80)
    
    maze_uni = create_tp2_maze(30, 30, obstacle_type="maze_pattern")
    maze_bi_di = BiDirectionalMaze(30, 30, grid=maze_uni.grid, rewards=maze_uni.rewards,
                                    start=maze_uni.start, goal=maze_uni.goal)
    maze_bi_a = BiDirectionalMaze(30, 30, grid=maze_uni.grid, rewards=maze_uni.rewards,
                                   start=maze_uni.start, goal=maze_uni.goal)
    
    path_uni_di = maze_uni.solve_dijkstra(return_explored=True)
    path_uni_a = maze_uni.solve(return_explored=True)
    path_bi_di = maze_bi_di.dijkstra_bidirectional(return_explored=True)
    path_bi_a = maze_bi_a.astar_bidirectional(return_explored=True)
    
    explored_uni_di = len(path_uni_di[1])
    explored_uni_a = len(path_uni_a[1])
    print(f"\nUnidirectional Dijkstra : {explored_uni_di} cellules explorées")
    print(f"Unidirectional A* : {explored_uni_a} cellules explorées")
    print(f"Bidirectional Dijkstra : {path_bi_di[3]} cellules explorées ({(1 - path_bi_di[3]/explored_uni_di)*100:.1f}% réduction)")
    print(f"Bidirectional A* : {path_bi_a[3]} cellules explorées ({(1 - path_bi_a[3]/explored_uni_a)*100:.1f}% réduction)")
    
    print("\n" + "="*80)
    print("TEST 5 : Comparaison des temps d'exécution")
    print("="*80)
    
    maze_uni = create_tp2_maze(30, 30, obstacle_type="maze_pattern")
    maze_bi_di = BiDirectionalMaze(30, 30, grid=maze_uni.grid, rewards=maze_uni.rewards,
                                    start=maze_uni.start, goal=maze_uni.goal)
    maze_bi_a = BiDirectionalMaze(30, 30, grid=maze_uni.grid, rewards=maze_uni.rewards,
                                   start=maze_uni.start, goal=maze_uni.goal)
    
    # Dijkstra unidirectional
    import time
    start = time.time()
    maze_uni.solve_dijkstra()
    t_uni_di = time.time() - start
    
    # A* unidirectional
    start = time.time()
    maze_uni.solve()
    t_uni_a = time.time() - start
    
    # Dijkstra bidirectional
    start = time.time()
    maze_bi_di.dijkstra_bidirectional()
    t_bi_di = time.time() - start
    
    # A* bidirectional
    start = time.time()
    maze_bi_a.astar_bidirectional()
    t_bi_a = time.time() - start
    
    print(f"\nUnidirectional Dijkstra : {t_uni_di*1000:.2f} ms")
    print(f"Bidirectional Dijkstra : {t_bi_di*1000:.2f} ms (ratio: {t_uni_di/t_bi_di:.2f}x)")
    print(f"\nUnidirectional A* : {t_uni_a*1000:.2f} ms")
    print(f"Bidirectional A* : {t_bi_a*1000:.2f} ms (ratio: {t_uni_a/t_bi_a:.2f}x)")


if __name__ == "__main__":
    test_comparison()
