import os
import uuid
import matplotlib.pyplot as plt

def generate_plot(voltages, times):
    # Adjust path to your static folder
    static_folder = os.path.join("app", "AestheticData")
    os.makedirs(static_folder, exist_ok=True)

    filename = f"plot_{uuid.uuid4().hex}.png"
    full_path = os.path.join(static_folder, filename)

    plt.figure()
    plt.plot(times, voltages, marker='o')
    plt.title("Voltage over Time")
    plt.xlabel("Time (s)")
    plt.ylabel("Voltage (V)")
    plt.grid(True)
    plt.savefig(full_path)
    plt.close()

    # Return URL for the image in your template
    return f"/AestheticData/{filename}"
