import math
class Inductor:
    def __init__(self, inductance):
        self.inductance = inductance  # Induktivität in Henry

    def get_impedance(self, frequency):
        return complex(0, 2 * math.pi * frequency * self.inductance)  # induktiver Blindwiderstand
