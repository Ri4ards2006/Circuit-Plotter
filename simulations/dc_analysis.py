def calculate_series_voltage(resistors, current):
     return sum(r.resistance for r in resistors) * current