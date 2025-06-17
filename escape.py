              #################@@@ Factory Shutdown Escape Game @@@##################

# This is a simple text-based escape game where the player navigates through rooms in a factory
# to find their way out. The player can move in four directions: North, South, East, and West.
# The game will start in the Break Room, and the player can exit the game by typing 'exit'.


rooms = {
    'Break Room': {'North': 'QA Lab', 'South': 'Manufacturing Line', 'East': 'Parts Inventory', 'West': 'AI Core'},
    'QA Lab': {'South': 'Break Room', 'East': 'Server Room'},
    'Server Room': {'West': 'QA Lab'},
    'Manufacturing Line': {'North': 'Break Room', 'East': 'Tool Crib'},
    'Tool Crib': {'West': 'Manufacturing Line'},
    'Parts Inventory': {'West': 'Break Room', 'North': 'Maintenance Bay'},
    'Maintenance Bay': {'South': 'Parts Inventory'},
    'AI Core': {'East': 'Break Room'}
}

# The game will start in the Break Room
current_room = 'Break Room'

print("****************************************************************************")
print("|                                                                          |")
print("|   Welcome to Factory Shutdown Escape                                     |")
print("|   To Move between rooms, type: go North, go South, go East, or go West   |")
print("|   Type 'exit' to quit the game                                           |")
print("|                                                                          |")
print("***************************************************************************")


# Escape game loop  
while current_room != 'exit':
    print("You are in the", current_room)
    command = input("Enter your move: ").strip()

    # The exit command to quit the game
    if command.lower() == 'exit':
        current_room = 'exit'
        print("Thanks for playing. Goodbye :)")
    # The move commands to navigate between rooms
    elif command.lower().startswith('go north'):
        if 'North' in rooms[current_room]:
            current_room = rooms[current_room]['North']
        else:
            print("You can't go that way!\n")
    elif command.lower().startswith('go south'):
        if 'South' in rooms[current_room]:
            current_room = rooms[current_room]['South']
        else:
            print("You can't go that way!\n")
    elif command.lower().startswith('go east'):
        if 'East' in rooms[current_room]:
            current_room = rooms[current_room]['East']
        else:
            print("You can't go that way!\n")
    elif command.lower().startswith('go west'):
        if 'West' in rooms[current_room]:
            current_room = rooms[current_room]['West']
        else:
            print("You can't go that way!\n")
    elif command.lower().startswith('go '):
        direction = command[3:].capitalize()

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!\n")
    # If user enter invalid input
    else:
        print("Invalid command. Please type something like 'go North' or 'exit'.\n")