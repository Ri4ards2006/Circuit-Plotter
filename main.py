from circuits.resistor import Resistor
from simulations.dc_analysis import calculate_series_voltage
from plots.plot_voltage import plot_voltage_over_time

r1 = Resistor(100)
r2 = Resistor(150)

strom = 0.02  # 20 mA

spannung = calculate_series_voltage([r1, r2], strom)

print(f"Gesamtspannung: {spannung:.2f} V")

# Plotten

zeiten = [0, 1, 2, 3, 4]
spannungen = [spannung * t / 4 for t in zeiten]

plot_voltage_over_time(spannungen, zeiten)
