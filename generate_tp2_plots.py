"""Generate TP2 benchmark plots for Typst report."""

import os
import matplotlib.pyplot as plt
import numpy as np


ASSETS_DIR = os.path.join("Document", "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

# Measured results from tests_bidirectional.py and benchmark_networkx_tp2.py
cases = ["10x10\nno obs", "10x10\nobs 0.2", "12x8\nvertical", "30x30\nmaze"]

# Explored nodes
dijkstra_uni = [99, 83, 80, 520]
dijkstra_bi = [92, 70, 76, 438]

astar_uni = [99, 47, 80, 160]
astar_bi = [92, 48, 70, 268]

# Runtime on 30x30 maze_pattern (ms)
algo_labels = ["Dijkstra uni", "Dijkstra bi", "A* uni", "A* bi", "NetworkX bi"]
times_ms = [1.99, 1.28, 0.66, 1.11, 1.25]

plt.style.use("seaborn-v0_8-whitegrid")

# Plot 1: Dijkstra explored nodes
x = np.arange(len(cases))
width = 0.36
fig, ax = plt.subplots(figsize=(9, 4.8), dpi=160)
ax.bar(x - width / 2, dijkstra_uni, width, label="Unidirectional", color="#1f77b4")
ax.bar(x + width / 2, dijkstra_bi, width, label="Bidirectional", color="#2ca02c")
ax.set_title("Dijkstra: explored nodes")
ax.set_ylabel("Explored nodes")
ax.set_xticks(x)
ax.set_xticklabels(cases)
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(ASSETS_DIR, "tp2_plot_dijkstra_explored.png"), bbox_inches="tight")
plt.close(fig)

# Plot 2: A* explored nodes
fig, ax = plt.subplots(figsize=(9, 4.8), dpi=160)
ax.bar(x - width / 2, astar_uni, width, label="Unidirectional", color="#9467bd")
ax.bar(x + width / 2, astar_bi, width, label="Bidirectional", color="#ff7f0e")
ax.set_title("A*: explored nodes")
ax.set_ylabel("Explored nodes")
ax.set_xticks(x)
ax.set_xticklabels(cases)
ax.legend()
fig.tight_layout()
fig.savefig(os.path.join(ASSETS_DIR, "tp2_plot_astar_explored.png"), bbox_inches="tight")
plt.close(fig)

# Plot 3: Runtime comparison on 30x30
fig, ax = plt.subplots(figsize=(9, 4.8), dpi=160)
bars = ax.bar(algo_labels, times_ms, color=["#1f77b4", "#2ca02c", "#9467bd", "#ff7f0e", "#d62728"])
ax.set_title("Runtime on 30x30 maze_pattern")
ax.set_ylabel("Time (ms)")
ax.set_ylim(0, max(times_ms) * 1.25)
for bar, value in zip(bars, times_ms):
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 0.03, f"{value:.2f}", ha="center", va="bottom", fontsize=9)
fig.tight_layout()
fig.savefig(os.path.join(ASSETS_DIR, "tp2_plot_runtime_30x30.png"), bbox_inches="tight")
plt.close(fig)

print("Plots generated in Document/assets")
