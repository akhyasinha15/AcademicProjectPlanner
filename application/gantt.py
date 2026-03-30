import matplotlib
matplotlib.use('Agg')   # FIX for Flask

import os
import matplotlib.pyplot as plt

def generate_gantt(plan):
    folder = "static/charts"
    os.makedirs(folder, exist_ok=True)

    phases = list(plan.keys())
    durations = list(plan.values())

    plt.figure()
    plt.barh(phases, durations)
    plt.xlabel("Weeks")
    plt.title("Project Gantt Chart")

    path = os.path.join(folder, "gantt.png")
    plt.savefig(path)
    plt.close()

    return path