
answer = input("Would you like to play? (yes/no)")

if answer.lower().strip() == "yes":

    answer = input("You reach a crossroads. Left or right?").lower().strip()
    if answer == "left":
        answer = input("A monster blocks your path, will you attack or run?")

        if answer == "attack":
            print("The monster attacks you, and you black out. Goodbye")
        else:
            print("The monster trips over, and you get away.")

        answer = input("You see a car and a plane, which will you take? (car/plane")

        if answer == "plane":
            print("You realise you are untrained for flight, and cannot fly. Goodbye.")
        else:
            print("You drive off happily. Goodbye!")

    elif answer == "right":
        answer = input("You wander through a forest and fall in a hunter's trap. Do you attempt to climb out "
                       "or wait for help? (climb/wait)")

        if answer == "climb":
            print("As you climb the pit, you slip on a root and fall, breaking your neck. Goodbye.")
        else:
            print("The hunter comes to heck his trap, and helps you out.")

    else:
        print("Invalid choice, goodbye.")

else:
    print("That's too bad")
