import random
import numpy as np

class Game2048:
    def __init__(self, demensions):
        self.demensions = demensions
        self.grid = np.array
        self.memory = []
        self.move_made = True
        self.score = 0
        self.potential = 0

    def start_game(self):
        self.new_game()

    def new_game(self):
        self.score = 0
        self.potential = 0
        self.__init_grid()
        self.__draw()


    def __init_grid(self):
        self.grid = np.zeros(
                (self.demensions, self.demensions),
                dtype = int
                )
        self.__add_value()
        self.move_made = True
        self.__add_value()
        self.__save_grid()



    def up(self):
        self.__save_grid()
        self.grid = np.transpose(self.grid)
        self.__colide_to_left()
        self.grid = np.transpose(self.grid)
        self.__update()

    def down(self):
        self.__save_grid()
        self.grid = np.transpose(self.grid)
        self.grid = np.fliplr(self.grid)
        self.__colide_to_left()
        self.grid = np.fliplr(self.grid)
        self.grid = np.transpose(self.grid)
        self.__update()

    def right(self):
        self.__save_grid()
        self.grid = np.fliplr(self.grid)
        self.__colide_to_left()
        self.grid = np.fliplr(self.grid)
        self.__update()

    def left(self):
        self.__save_grid()
        self.__colide_to_left()
        self.__update()

    def undo(self):
        if len(self.memory) > 0:
            rec_grid = self.memory.pop()
            self.grid = rec_grid
            self.__draw()

    def check(self):
        for state in self.memory:
            print(state)

    def __colide_to_left(self):
        def move_zeros(row):
            end = self.demensions - 1
            i = 0
            while i < end:
                if row[i] == 0:
                    j = i
                    while j < end:
                        if row[i+1] != 0:
                            self.move_made = True

                        row[j], row[j+1] = row[j+1], row[j]
                        j += 1
                    end -=1
                else:
                    i += 1
        for row in self.grid:
            end = self.demensions - 1
            move_zeros(row)
            i = 0
            while i < end:
                if row[i] == row[i+1] and row[i] != 0:
                    row[i] *= 2
                    row[i+1] = 0
                    i += 2
                    self.move_made = True
                else:
                    i += 1
            move_zeros(row)


    def __add_value(self):
        if self.move_made:
            result = np.where(self.grid == 0.)
            coordinates = list(zip(result[0], result[1]))
            random_coor = coordinates[np.random.randint(0,len(coordinates))]

            value = 4 if np.random.random() <= 0.1 else 2

            self.grid[random_coor[0]][random_coor[1]] = value

            self.score += value
            self.move_made = False

    def __update(self):
        if self.move_made:
            self.__add_value()
            self.__calculate_potential()
            self.__draw()

    def __draw(self):
        print('')
        for i in self.grid:
            for j in i:
                if j == 0:
                    print('', end='\t')
                else:
                    print(j, end='\t')
            print("")
        print('')
        print(f"Score: {self.score}\tPotential: {self.potential}\nUndo's: {len(self.memory)}")


    def __save_grid(self):
        grid = np.copy(self.grid)
        if len(self.memory) == 5:
            self.memory.pop(0)
            self.memory.append(grid)
        else:
            self.memory.append(grid)

    def __calculate_potential(self):
        self.potential = 0


    def __game_over(self):
        print("Game Over")

