def calculate_series_voltage(components, current, frequency=50):
    total_voltage = 0 + 0j  # komplexe Zahl
    for comp in components:
        impedance = comp.get_impedance(frequency)
        voltage = current * impedance
        total_voltage += voltage
    return total_voltage
