from module import Pet

name = input("Enter a name for your pet: ")


hunger = 50
happeness = 50
energy = 50
pet = Pet(name, hunger, happeness, energy)
while True:
    print("Commands: Feed | Play | Sleep | Check Health | Status | Quit ")
    command = input("What would you like to do next? ")

    if command == "Feed":
        amount = int(input ("How much to feed? "))
        print(feed(pet, amount))
    elif command == "Play":
        amount = int(input ("How much play? "))
        print(play(pet, amount))
    elif command == "Sleep":
        amount = int(input ("How long to sleep? "))
        print(sleep(pet, amount))
    elif command == "Check Health":
        print(pet.check_health())
    elif command == "Status":
        print(status(pet))
    elif command == "Quit":
        print("Quitting the simulator")
        break
    else:
        print("I don't recognize that command. Try again.")
    print(pet.status())
    