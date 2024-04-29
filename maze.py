def maze():
    import time

    #The maze in characters
    MAZE = [
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
        ["#", " ", "#", " ", "#", " ", "#", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", " ", " ", "#", " ", "#", "#", "#", " ", "#"],
        ["#", " ", " ", " ", "#", "#", "#", " ", " ", " ", " ", " ", "#"],
        ["#", " ", "#", " ", " ", " ", " ", " ", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", "#", "#", "#", " ", "#", " ", " ", " ", "#"],
        ["#", " ", "#", " ", "#", " ", " ", " ", "#", "#", "#", " ", "#"],
        ["#", " ", "#", " ", "#", "#", "#", " ", "#", " ", "#", " ", "#"],
        ["#", " ", " ", " ", " ", " ", " ", " ", " ", " ", "#", "E", "#"],
        ["#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#", "#"],
    ]

    #Moving player bsed on input
    def move_player(MAZE, player_position):
        try:
            direction = input("Enter your move (w/a/s/d): ")
            x, y = player_position
            if direction == "w":
                y -= 1
            elif direction == "a":
                x -= 1
            elif direction == "s":
                y += 1
            elif direction == "d":
                x += 1
            else:
                print("Invalid move!")
                return player_position

            if MAZE[y][x] == "#":
                print("You hit a wall!")
                return player_position
            elif MAZE[y][x] == "E":
                print("You found the exit!")
                return None  # Game over
            else:
                return (x, y)

        except:
            print("Invalid input")

    #Initializing game and printing board with remaining time after each input
    def game_loop(MAZE):
        global result
        start_time = time.time()
        player_position = (1, 1)  # Starting position
        MAZE[player_position[1]][player_position[0]] = "P"

        while True:
            print_maze(MAZE)
            player_position = move_player(MAZE, player_position)
            if player_position is None:
                result = True
                break
            MAZE[player_position[1]][player_position[0]] = "P"
            if time.time() - start_time > 30:
                print("Time's up!")
                result = False
                break
            print(30 - int(time.time() - start_time), "seconds left")

    def print_maze(MAZE):
        for row in MAZE:
            print("".join(row))

    game_loop(MAZE)
    return result
