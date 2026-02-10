# This is an an incomplete 
class Pet:
    def __init__(self, name, hunger, happiness, energy):
        # Add initialize code here
        self.name = name
        self.hunger = hunger
        self.happiness = happiness
        self.energy = energy
    def feed(self, amount):
        # Add feed code here
        self.hunger += amount
        return f"{self.name} has been fed. Hunger increased by {amount}."
    def play(self, duration):
        self.happiness += duration
        self.energy -= duration
        return f"{self.name} has played for {duration} minutes."
    def sleep(self,duration):
        self.energy += duration
        self.hunger -= duration // 2
        return f"{self.name} has slept for {duration} minutes."
    def status(self):
        return f"Name: {self.name}, Hunger: {self.hunger}, Happiness: {self.happiness}, Energy: {self.energy}"
    