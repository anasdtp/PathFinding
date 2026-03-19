"""Generate TP2 action plots (exploration + final path) for classic/bidirectional Dijkstra and A*."""

import os
import numpy as np
import matplotlib.pyplot as plt

from main import create_complete_maze
from Maze import Maze
from bidirectional import BiDirectionalMaze


ASSETS_DIR = os.path.join("Document", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)


def make_base_rgb(maze):
    h, w = maze.height, maze.width
    img = np.ones((h, w, 3), dtype=float)
    img[:] = [0.96, 0.96, 0.96]
    img[maze.grid == 1] = [0.15, 0.15, 0.15]
    return img


def overlay_cells(img, cells, color, alpha=0.5):
    for r, c in cells:
        if 0 <= r < img.shape[0] and 0 <= c < img.shape[1]:
            img[r, c] = (1 - alpha) * img[r, c] + alpha * np.array(color)


def draw_panel(ax, maze, path, explored, title, explored2=None):
    img = make_base_rgb(maze)

    if explored:
        overlay_cells(img, explored, color=[0.25, 0.45, 0.95], alpha=0.45)
    if explored2:
        overlay_cells(img, explored2, color=[0.25, 0.75, 0.35], alpha=0.45)
    if path:
        overlay_cells(img, path, color=[0.98, 0.60, 0.05], alpha=0.95)

    sr, sc = maze.start
    gr, gc = maze.goal
    img[sr, sc] = [0.1, 0.85, 0.1]
    img[gr, gc] = [0.9, 0.1, 0.1]

    ax.imshow(img, interpolation="nearest")
    ax.set_title(title, fontsize=11)
    ax.set_xticks([])
    ax.set_yticks([])


# Shared scenario for all 4 algorithms
maze_ref = create_complete_maze(
    30,
    30,
    obstacle_type="maze_pattern",
    step_cost=-1.0,
    goal_reward=-1.0,
    add_bonuses=False,
)

maze_uni = Maze(
    maze_ref.width,
    maze_ref.height,
    grid=maze_ref.grid,
    rewards=maze_ref.rewards,
    start=maze_ref.start,
    goal=maze_ref.goal,
)
maze_bi = BiDirectionalMaze(
    maze_ref.width,
    maze_ref.height,
    grid=maze_ref.grid,
    rewards=maze_ref.rewards,
    start=maze_ref.start,
    goal=maze_ref.goal,
)

# Unidirectional algorithms
path_dij_uni, explored_dij_uni = maze_uni.solve_dijkstra(return_explored=True)
path_ast_uni, explored_ast_uni = maze_uni.solve(return_explored=True)

# Bidirectional algorithms (with explored sets)
res_dij_bi = maze_bi.dijkstra_bidirectional(return_explored=True, return_sets=True)
path_dij_bi = res_dij_bi[0]
explored_dij_bi_f = res_dij_bi[4]
explored_dij_bi_b = res_dij_bi[5]

res_ast_bi = maze_bi.astar_bidirectional(return_explored=True, return_sets=True)
path_ast_bi = res_ast_bi[0]
explored_ast_bi_f = res_ast_bi[4]
explored_ast_bi_b = res_ast_bi[5]

fig, axes = plt.subplots(2, 2, figsize=(11, 10), dpi=170)

# Top row: Dijkstra
_draw_title = "explored + path"
draw_panel(
    axes[0, 0],
    maze_ref,
    path_dij_uni,
    explored_dij_uni,
    f"Dijkstra classique ({_draw_title})",
)
draw_panel(
    axes[0, 1],
    maze_ref,
    path_dij_bi,
    explored_dij_bi_f,
    f"Dijkstra bidirectionnel ({_draw_title})",
    explored2=explored_dij_bi_b,
)

# Bottom row: A*
draw_panel(
    axes[1, 0],
    maze_ref,
    path_ast_uni,
    explored_ast_uni,
    f"A* classique ({_draw_title})",
)
draw_panel(
    axes[1, 1],
    maze_ref,
    path_ast_bi,
    explored_ast_bi_f,
    f"A* bidirectionnel ({_draw_title})",
    explored2=explored_ast_bi_b,
)

fig.suptitle("Illustrations du pathfinding en action (meme labyrinthe 30x30)", fontsize=14)
fig.tight_layout(rect=[0, 0.02, 1, 0.97])
out_path = os.path.join(ASSETS_DIR, "tp2_plot_pathfinding_action_all.png")
fig.savefig(out_path, bbox_inches="tight")
plt.close(fig)

print(f"Saved: {out_path}")
