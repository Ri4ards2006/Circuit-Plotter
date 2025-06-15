import matplotlib.pyplot as plt

def plot_voltage_over_time(spannungen, zeiten):
    plt.plot(zeiten, spannungen, marker='o')
    plt.title("Spannung über Zeit")
    plt.xlabel("Zeit (s)")
    plt.ylabel("Spannung (V)")
    plt.grid(True)
    plt.show()
