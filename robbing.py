def robbery():
    import os
    import random
    import msvcrt
    import time

    class PacmanGame:
        #Randomly chooses position of "money bundle"
        def __init__(self):
            self.height = 10
            self.width = 20
            self.pacman_pos = [self.height // 2, self.width // 2]
            self.food_pos = [
                random.randint(0, self.height - 1),
                random.randint(0, self.width - 1),
            ]
            self.score = 0

        #Cheking and adding score
        def draw(self):
            os.system("cls" if os.name == "nt" else "clear")
            for y in range(self.height):
                for x in range(self.width):
                    if [y, x] == self.pacman_pos:
                        print("P", end=" ")
                    elif [y, x] == self.food_pos:
                        print("*", end=" ")
                    else:
                        print(".", end=" ")
                print()
            print("Score:", self.score)

        #Moving token according to user input
        def move_pacman(self, direction):
            if direction == "w":
                self.pacman_pos[0] = (self.pacman_pos[0] - 1) % self.height
            elif direction == "s":
                self.pacman_pos[0] = (self.pacman_pos[0] + 1) % self.height
            elif direction == "a":
                self.pacman_pos[1] = (self.pacman_pos[1] - 1) % self.width
            elif direction == "d":
                self.pacman_pos[1] = (self.pacman_pos[1] + 1) % self.width
            else:
                print("invalid input")

        #Checking if points have been collected and adding new points to be collected if so
        def check_collision(self):
            if self.pacman_pos == self.food_pos:
                self.score += 1
                self.food_pos = [
                    random.randint(0, self.height - 1),
                    random.randint(0, self.width - 1),
                ]

        #Constantly checks various conditions throughout
        def play(self):
            start_time = time.time()
            while True:
                self.draw()
                self.check_collision()
                direction = self.get_char()
                if time.time() - start_time > 30:
                    print("Time's up!")
                    break
                elif direction in ["w", "a", "s", "d"]:
                    self.move_pacman(direction)

        def get_char(self):
            try:

                char = msvcrt.getch().decode().lower()

            except:
                print("invalid input")
            else:
                if char == "\x03":
                    exit()
                return char

    game = PacmanGame()
    game.play()
    if game.score >= 10:
        return True
    else:
        return False
