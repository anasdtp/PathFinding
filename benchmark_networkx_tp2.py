"""
TP2 - Comparaison avec NetworkX bidirectional_dijkstra
"""

import time
import networkx as nx

from main import create_complete_maze
from bidirectional import BiDirectionalMaze


def maze_to_graph(maze):
    g = nx.Graph()
    for i in range(maze.height):
        for j in range(maze.width):
            if not maze.is_passable(i, j):
                continue
            g.add_node((i, j))
            for ni, nj in maze.get_neighbors(i, j):
                # Poids unitaire pour rester cohérent avec le benchmark TP2
                g.add_edge((i, j), (ni, nj), weight=1)
    return g


def main():
    maze = create_complete_maze(
        30,
        30,
        obstacle_type="maze_pattern",
        step_cost=-1.0,
        goal_reward=-1.0,
        add_bonuses=False,
    )

    bi = BiDirectionalMaze(
        30,
        30,
        grid=maze.grid,
        rewards=maze.rewards,
        start=maze.start,
        goal=maze.goal,
    )

    # Notre implementation
    t0 = time.time()
    path_bi, cost_bi, elapsed_bi, explored_bi = bi.dijkstra_bidirectional(return_explored=True)
    t_ours = time.time() - t0

    # NetworkX
    g = maze_to_graph(maze)
    t1 = time.time()
    dist_nx, path_nx = nx.bidirectional_dijkstra(g, maze.start, maze.goal)
    t_nx = time.time() - t1

    print("=== COMPARAISON AVEC NETWORKX ===")
    print(f"Notre Dijkstra bidirectionnel: longueur={len(path_bi) if path_bi else None}, cout={cost_bi:.2f}, temps={t_ours*1000:.2f} ms, explores={explored_bi}")
    print(f"NetworkX bidirectional_dijkstra: longueur={len(path_nx)}, cout={dist_nx:.2f}, temps={t_nx*1000:.2f} ms")

    if path_bi:
        print(f"Chemins de meme longueur: {len(path_bi) == len(path_nx)}")


if __name__ == "__main__":
    main()
