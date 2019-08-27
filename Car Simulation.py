command = " "
started = False
print("""This game is a simulation of a car game. 
        START - To start the game.
        STOP - To stop the game.
        QUIT - To quit the game.""")
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car is already started.")
        else:
            started = True
            print("Car started ready to go...")
    elif command == "stop":
        if not started:
            print("Car is already stopped")
        else:
            started = False
            print("Oops you stopped the car")
    elif command == "help":
        print("""
start - to start the car.
stop - to stop the car.
quit - to quit the game.""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand.")
