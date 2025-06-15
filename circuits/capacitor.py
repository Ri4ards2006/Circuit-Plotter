import math
class Capacitor:
    def __init__(self, capacitance):
        self.capacitance = capacitance  # Kapazität in Farad

    def get_impedance(self, frequency):
        if frequency == 0:
            return complex(float('inf'))  # Bei Gleichstrom sperrt der Kondensator (unendlich hoher Widerstand)
        else:
            return complex(0, -1 / (2 * math.pi * frequency * self.capacitance))  # kapazitiver Blindwiderstand
