# This is an an incomplete 
class Pet:
    def __init__(self, name):
        # Add initialize code here
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def status(self):
        return f"Name: {self.name}, Hunger: {self.hunger} | Happiness: {self.happiness} | Energy: {self.energy} |"
    def feed(self, amount):
        # Add feed code here
        self.hunger = self.hunger - int(amount)
        return f"{self.name} has been fed. Hunger decreased by {amount}."
    def play(self, duration, amount):
        self.happiness = self.happiness + int(amount)
        self.energy = self.energy - int(duration)
        return f"{self.name} has played for {duration} minutes and loses {amount}"
    def sleep(self,duration):
        self.energy = self.energy + int(duration)
        
        return f"{self.name} has slept for {duration} minutes and gains energy."
    def check_health(self):
        if (self.hunger > 70):
          return f"{self.name} is hungry."
        elif (self.hunger > 20):
           return f"{self.name} is starving, feed it before it dies."
        elif (self.energy > 30):
          return f"{self.name} is tired."
        elif (self.energy > 5):
           return f"{self.name} is exhauseted, it needs rest."
        elif (self.happiness > 50):
          return f"{self.name} is becoming depressed."
        elif (self.happiness > 10):
           return f"{self.name} is depressed, play with it."
        else:
           return f"{self.name} is healthy."