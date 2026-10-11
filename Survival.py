import random 

MAX_STAT = 100

health = 100 
hunger = 100
thirst = 100
day = 1

inventory = {
    "Water" : 2,
    "Food" : 1,
    "Wood" : 0,
    "Medicine" : 0,
}

print("=" * 40)
print("               SURVIVE: THE UNKNOWN")
print("=" * 40)
print("\nYou wake up in a mysterious forest.")
print("Your goal: survive fpr 10 days!")
print("Every choice matters. Good luck...\n")


name = input ("What is your survivor's name?")
print(f"\nWelcome,{name}. Your adventure begins...\n")


def show_status():
    print("\n" + "-" * 40)
    print(f"DAY: {day}/10")
    print(f"Health: {health}/100")
    print(f"Hunger: {hunger}/100")
    print(f"Thirst: : {thirst}/100")
    print("\nBACKPACK")

    for item, amoun6 in inventory.items():
        print(f"{item}: {amount}")
    
    print("-" * 40)


def change_stat(stat,amount):
    return max(0, min(MAX_STAT, stat + amount))


def explore():
    global health, hunger, thirst 
    
    event = random.choice(["food", "wood", "cabin", "storm", "nothing"])

    if event == "food":
        inventory["Food"] += 1
        print("\nYou discover some packeged food in an abandoned campsite!")

    elif event == "wood":
        inventory["Wood"] +=2
        print("\nYou collect two useful peices of wood.")

    elif event == "cabin": 
        print("\nYou discover an old cabin hidden among the trees!")
        if random.choice([True, False]):
            inventory["Medicine"] +=1
            print("Inside you find some medicine!")
        else:
            inventory["Wood"] +=1
            print("You find a sturdy peice of wood.")

    elif event == "storm":
        health = change_stat(health, -10)
        print("\nA sudden storm catches you outside!")
        print("You lose 10 health.")

    else:
        print("/nYou find a mysterious trail leading deeper in the forest.")


def gather():
    inventory["Wood"] += random.randint(1, 3)
    print("\nYou gather wood for a future shelter.")

def eat(): 
    global hunger 

    if inventory["Food"]>0:
        hunger = change_stat (hunger, 30)
        print("\nYou eat some food and feel less hungry!")
    else:
        print("\nYou have no food in your backpack")

def drink():
    global thirst 
    
    
    if inventory["Water"] > 0: 
        inventory["Water"] -= 1
        thirst = change_stat(thirst, 35)
        print("\nYou drink some water and feel refreshed!")
    else:
        print("\nYou have no water left")



def rest():
    global health 
    

    if inventory["Wood"]>=2:
        inventory["Wood"]-= 2
        health = change_stat(health, 15)
        print("\nYou build a small shelter and rest!")
        print("Your health improves by 15!")
    else:
        health = change_stat(health, 15)
        print("\nYou rest beneath a tree.")
        print("You recover 5 health, but have no shelter.")


def random_event():
    global health

    if random.randint(1,5) == 1:
        print("\nEVENT: You hear a strange noise nearby...")
        print("Stay alert and avoid trouble...")

    elif random.randint(1,8) ==1:
        inventory["Medicine"] += 1
        print("\nLUCKY FIND: You discover a first-aid kit!")


while health > 0 and day <=10:
    show_status()

    print("\nWhat would you like to do")
    print("1.Explore the forest") 
    print("2.Gather wood")
    print("3.Eat food")
    print("4.Drink Water")
    print("5.Rest or build a shelter")
    print("6.View backpack")
    print("7.Quit Game")


    choice = input("\nEnter your choice (1-7):").strip()
    if choice == "1":
        explore()
    elif choice == "2":
        gather()
    elif choice == "3":
        eat()
    elif choice == "4":
        drink()
    elif choice == "5":
        rest()
    elif choice == "6":
        print("\nYOUR BACKPACK:")
        for item, amount in inventory.items():
            print(f"{item}:{amount}")
        continue
    elif choice == "7":
        print("\nYou leave the forest for now...")
        break
    else:
        print("\nThat is not a valid choice.Try again.")
        continue
    #surviving takes energy and resources
    hunger = change_stat(health,-10)
    thirst = change_stat(thirst, -10)

    if hunger == 0:
        health = change_stat(health, -15)
        print("You are dehydrated, You lose 15 health.")

    random_event()


    if health <= 0:
        print("\nYou Died...")
        print("Game Over...")
        break

    # A new day begins after every three actions
    if choice != "6":
        print("\nYou continue through the forest...")
        # We will improve the day system as the day grows
        day += 1


    if health > 0 and day >10:
        print("\n" + "=" * 40)
        print("YOU SURVIVED THE FOREST")
        print(f"Congratulations,{name}!")
        print("You survived all 10 day!")
        print("=" * 40)



