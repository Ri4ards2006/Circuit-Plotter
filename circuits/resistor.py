class Resistor:
    def __init__(self, resistance):
        self.resistance = resistance  # Widerstand in Ohm

    def get_impedance(self, frequency):
        return complex(self.resistance, 0)  # Impedanz ist reell (Widerstand, kein Phasenwinkel)
