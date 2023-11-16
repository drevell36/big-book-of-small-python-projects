import copy, random, sys, time

# Set up the constants:
WIDTH = 70  # Width of the cell grid.
HEIGHT = 20  # Height of the call grid.

# (!) Try changing ALIVE to '#' or another character:
ALIVE = "0"  # The character representing a living cell.
# (!) Try changing DEAD to '. or another character:
DEAD = " "  # The character representing a dead cell.

# (!) Try changing ALIVE to '|' and DEAD to '-'.

# The cells and nextCells are dictionaries for the state of the game.
# Their keys are (x, y) tuples and their values are one of the ALIVE
# or DEAD values.
nextCells = {}
# Put random dead and alive cells into nextCells:
for x in range(WIDTH):  # Loop over every possible column.
    for y in range(HEIGHT):  # Loop over every possible row.
        # 50/50 chance for starting cells being alive or dead.
        if random.randint(0, 1) == 0:
            nextCells[(x, y)] = ALIVE  # Add a living cell.
        else:
            nextCells[(x, y)] = DEAD  # Add a dead cell.

while True:  # Main program loop.
    # Each iteration of this loop is a step of the simulation.

    print("\n " * 50)  # Separate each step with newlines.
    cells = copy.deepcopy(nextCells)

    # Print cells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            print(cells[x, y], end="")  # Print the # or space.
        print()  # Print a new line at the end of the row.
    print("Press CTRL-C to quit.")

    # Calculate the next step's cells based on current step's cells:
    for x in range(WIDTH):
        for y in range(HEIGHT):
            # Get the neighbouring coordinates of (x, y), even if they
            # wrap around the edge:
            left = (x - 1) % WIDTH
            right = (x + 1) % WIDTH
            above = (y - 1) % HEIGHT
            below = (y + 1) % HEIGHT

            # Count the number of living neighbours:
            numNeighbours = 0
            if cells[(left, above)] == ALIVE:
                numNeighbours += 1  # Top-left neighbour is alive.
            if cells[(x, above)] == ALIVE:
                numNeighbours += 1  # Top neighbour is alive.
            if cells[(right, above)] == ALIVE:
                numNeighbours += 1  # Top-right neighbour is alive.
            if cells[(left, y)] == ALIVE:
                numNeighbours += 1  # Left neighbour is alive.
            if cells[(right, y)] == ALIVE:
                numNeighbours += 1  # Right neighbour is alive.
            if cells[(left, below)] == ALIVE:
                numNeighbours += 1  # Bottom-left neighbour is alive.
            if cells[(x, below)] == ALIVE:
                numNeighbours += 1  # Bottom neighbour is alive.
            if cells[(right, below)] == ALIVE:
                numNeighbours += 1  # Right neighbour is alive.

            # Set cell based on Conway's Game of Life rules:
            if cells[(x, y)] == ALIVE and (numNeighbours == 2 or numNeighbours == 3):
                # Living cells with 2 or 3 neighbours stay alive:
                nextCells[(x, y)] = ALIVE
            elif cells[(x, y)] == DEAD and numNeighbours == 3:
                # Dead cells with 3 neighbours become alive:
                nextCells[(x, y)] = ALIVE
            else:
                # Everything else dies or stays dead:
                nextCells[(x, y)] = DEAD

    try:
        time.sleep(1)  # Add a 1 second pause to reduce flickering.
    except KeyboardInterrupt:
        print("Conway's Game of Life")
        sys.exit()  # When Ctrl-C is pressed, end the program
