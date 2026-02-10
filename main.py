
from module import Pet


print("What is your pet's name?")
name = input("name:")

hunger = 50
happeness = 50
energy = 50
pet = Pet(name, hunger, happeness, energy)
print(pet.status())
print(pet.feed(10))
print(pet.play(15))
print(pet.status())
print(pet.sleep(20))
print(pet.status())