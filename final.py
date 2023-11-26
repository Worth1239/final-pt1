def game():
    print("Okay! Let us begin")
    y = input("What is your name? ")
    name = y

    print(f"Alright {name}, let's go!")
    print()
    print()
    print()
    print("You wake up at 7:00 AM, like always. You have work in a few hours, and you really don't feel like going")
    while True:
        first_choice = input("What will you do? (A: Go to work, B: Don't go to work) ")
        if first_choice.upper() == "A":
            print("You get ready and go to work")
            while True:
                a = input("How do you get to work? (A: Drive, B: Public transport/walk) ")
                if a.upper() == "A":
                    print("You get into your 2004 Toyota corolla.")
                elif a.upper() == "B":
                    print("You hop on the bus and see there are seats in the front and back.")
                else:
                    print("Invalid, try again.")
                    continue
                    while True:
                        b = input("Where do you want to sit? (A:Front, B:Back) ")
                        if b.upper() == "A":
                            print("You take seat at the very front of the bus.")
                        elif b.upper() == "B":
                            print("You take a seat at the back of the bus")
                        else:
                            print("Invalid, try again.")
                            continue
        elif first_choice.upper() == "B":
            print("")
        else:
            print("Invalid, try again.")
            continue


x = input("Hello! Welcome to my story game! Would you like to play? ")
if x.lower() == "yes":
    game()
else:
    quit()
