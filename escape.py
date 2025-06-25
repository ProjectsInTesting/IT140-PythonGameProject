#################@@@ Factory Shutdown Escape Game @@@##################

# This is a simple text-based adventure game called "Factory Shutdown Escape."
# The player navigates through rooms in a factory to collect 6 important tools
# and shut down a rogue AI in order to escape.
# The player can move in four directions: North, South, East, and West.
# N = Go North     S = Go South     E = Go East     W = Go West
# The game will start in the Break Room, and the player can exit the game at any time by typing 'exit'.
# Goal: Collect all 6 tools before entering the AI Core.
# If you enter the AI Core without all 6 tools, the rogue AI will catch you and you lose the game.

#################

# This Function will show the game instructions
def show_instructions():
    print("****************************************************************************")
    print("*  Welcome to <<< Factory Shutdown Escape >>>                              *")
    print("*  Collect all 6 tools to shut down the rogue AI and escape the factory.   *")
    print("*  To Move between rooms use these Commands:                               *")
    print("*       N = Go North     S = Go South     E = Go East     W = Go West      *")
    print("*  To collect an item: type 'get [item]' (example: get wrench)             *")
    print("*  Type 'exit' to quit the game.                                           *")
    print("****************************************************************************\n")


# This Function will show the player's status
def show_status(current_room, inventory, rooms):
    print(f"You are in the {current_room}")
    print(f"Inventory: {inventory}")
    if "item" in rooms[current_room]:
        print(f"You see a {rooms[current_room]['item']}")
    print("--------------------------------------------------")


# The Main game function
def main():
    # Here is a Dictionary linking rooms and placing items in rooms
    rooms = {
        'Break Room': {'North': 'QA Lab', 'South': 'Manufacturing Line', 'East': 'Parts Inventory', 'West': 'AI Core'},# No item in this rom.
        'QA Lab': {'South': 'Break Room', 'East': 'Server Room', 'item': 'Safety Goggles'},
        'Server Room': {'West': 'QA Lab', 'item': 'Circuit Board'},
        'Maintenance Bay': {'South': 'Parts Inventory', 'item': 'Override Key'},
        'Parts Inventory': {'West': 'Break Room', 'North': 'Maintenance Bay', 'item': 'Backup Chip'},
        'Tool Crib': {'West': 'Manufacturing Line', 'item': 'Voltage Tester'},
        'Manufacturing Line': {'North': 'Break Room', 'East': 'Tool Crib', 'item': 'Wrench'},
        'AI Core': {'East': 'Break Room'} # No item in this room
    }

    current_room = 'Break Room'
    inventory = []

    show_instructions()

    while True:
        show_status(current_room, inventory, rooms)

        command = input("Enter your move: ").strip().lower()

        if command == 'exit':
            print("Thanks for playing. See you next time :)")
            break

        elif command in ['n', 's', 'e', 'w']:
            direction = {'n': 'North', 's': 'South', 'e': 'East', 'w': 'West'}[command]
            if direction in rooms[current_room]:
                current_room = rooms[current_room][direction]
            else:
                print("Oops! You can't go that way!\n")

        elif command.startswith("get "):
            item_requested = command[4:]
            if "item" in rooms[current_room] and rooms[current_room]['item'].lower() == item_requested:
                if item_requested not in inventory:
                    inventory.append(item_requested)
                    print(f"{item_requested.capitalize()} has been added to your inventory.\n")
                    del rooms[current_room]['item']
                else:
                    print("You already have this item.\n")
            else:
                print("There is no such item here to get.\n")

        else:
            print("Invalid input. Please use N, S, E, W or 'get [item]' or 'exit'.\n")

        # Checking for winning or losing conditions
        if current_room == 'AI Core':
            if len(inventory) == 6:
                print("\nCongratulations! you have collected all tools and shut down the rogue AI. You win!")
            else:
                print("\nNoooooo :( You have entered the AI Core without all tools. \n The rogue AI got you. GAME OVER!")
            print("Thanks for playing <<< Factory Shutdown Escape >>>")
            break


# Run the game
if __name__ == "__main__":
    main()