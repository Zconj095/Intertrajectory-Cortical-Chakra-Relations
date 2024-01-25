class Chakra:
    def __init__(self, name, gland, hormones, frequency):
        self.name = name
        self.gland = gland
        self.hormones = hormones
        self.frequency = frequency
        self.active = False

    def activate(self):
        self.active = True
        # Additional logic for effects on human EM field and Ki

# Example instantiation
root_chakra = Chakra("Root Chakra", "Adrenal Glands", ["Cortisol", "Adrenaline", "Noradrenaline"], 20-50)

# Simulate chakra activation
root_chakra.activate()
# Implement further logic based on activation