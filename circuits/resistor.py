class Resistor:
    def __init__(self, resistance_ohm):
        self.resistance = resistance_ohm

    def voltage(self, current_amps):
        return self.resistance * current_amps
