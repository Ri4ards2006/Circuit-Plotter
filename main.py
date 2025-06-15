from app import Resistor
from app import Capacitor
from app import Inductor
from simulations.ac_analysis import calculate_series_voltage
from plots.plot_voltage import plot_voltage_over_time

r1 = Resistor(100)
c1 = Capacitor(1e-6)  # 1 uF
l1 = Inductor(1e-3)   # 1 mH

strom = 0.02  # 20 mA

frequency = 50  # 50 Hz Wechselstrom

spannung = calculate_series_voltage([r1, c1, l1], strom, frequency)

print(f"Gesamtspannung : {spannung.real:.2f} V (Realteil)")

# Zeitwerte für Plot
zeiten = [0, 1, 2, 3, 4]

# Spannung linear über Zeit (Realteil)
spannungen = [spannung.real * t / 4 for t in zeiten]

plot_voltage_over_time(spannungen, zeiten)
