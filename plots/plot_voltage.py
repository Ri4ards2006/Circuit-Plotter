import matplotlib.pyplot as plt
import uuid
import os

def generate_plot(voltages, times):
    filename = f"static/plot_{uuid.uuid4().hex}.png"
    full_path = os.path.join("app", filename)

    plt.figure()
    plt.plot(times, voltages, marker='o')
    plt.title("Voltage over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.savefig(full_path)
    plt.close()

    return '/' + filename  # for use in HTML
