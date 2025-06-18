              #################@@@ Factory Shutdown Escape Game @@@##################

# This is a simple text-based escape game where the player navigates through rooms in a factory
# to find their way out. The player can move in four directions: North, South, East, and West.
# N = Go North     S = Go South     E = Go East     W = Go West
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
print("|   To Move between rooms use these Commands:                              |")
print("|       N = Go North     S = Go South     E = Go East     W = Go West      |")
print("|   Type 'exit' to quit the game                                           |")
print("|                                                                          |")
print("***************************************************************************")


# Escape game loop  
while current_room != 'exit':
    print("You are in the", current_room,"\n")
    command = input("Enter your move (N/S/E/W or exit): ").strip().lower()

    # The exit command to quit the game
    if command.lower() == 'exit':
        current_room = 'exit'
        print("Thanks for playing. Goodbye :)")

    # The move commands to navigate between rooms
    elif command in ['n', 's', 'e', 'w']:
        direction = {'n': 'North', 's': 'South', 'e': 'East', 'w': 'West'}[command]
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way!\n")

    # If the user enter invalid input
    else:
        print("Invalid command. Please type N, S, E, W, or exit.\n")