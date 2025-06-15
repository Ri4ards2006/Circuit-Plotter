from sympy.physics.units import frequency


def calculate_series_voltage(components, current):
    total_voltage = 0.0
    for comp in components:
        impedance = comp.get_impedance(frequency=0)
        if isinstance(impedance, complex):
            impedance = abs(impedance)  # DC Impedanz sollte real sein
        total_voltage += impedance * current
    return total_voltage
