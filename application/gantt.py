import matplotlib
matplotlib.use('Agg')

import os
import matplotlib.pyplot as plt

def generate_gantt(plan):
    folder = "static/charts"
    os.makedirs(folder, exist_ok=True)

    phases = list(plan.keys())
    durations = list(plan.values())

    # 🔥 SMALLER FIGURE SIZE
    plt.figure(figsize=(6, 3))   # width, height

    plt.barh(phases, durations)

    plt.xlabel("Weeks")
    plt.title("Project Timeline")

    plt.tight_layout()   # 🔥 removes extra spacing

    path = os.path.join(folder, "gantt.png")
    plt.savefig(path, dpi=80)   # smaller image
    plt.close()

    return path