import random
import numpy as np
from itertools import cycle
from pynput import keyboard

class Game2048:
    def __init__(self, demensions):
        self.demensions = demensions
        self.grid = []
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
        self.__add_value()
        self.__save_grid()



    def up(self):
        self.grid = np.transpose(self.grid)
        self.__colide_to_left()
        self.grid = np.transpose(self.grid)
        self.__update()

    def down(self):
        self.grid = np.transpose(self.grid)
        self.grid = np.fliplr(self.grid)
        self.__colide_to_left()
        self.grid = np.fliplr(self.grid)
        self.grid = np.transpose(self.grid)
        self.__update()

    def right(self):
        self.grid = np.fliplr(self.grid)
        self.__colide_to_left()
        self.grid = np.fliplr(self.grid)
        self.__update()

    def left(self):
        self.__colide_to_left()
        self.__update()

    def __colide_to_left(self):
        def move_zeros(row):
            end = 3
            i = 0
            while i < end:
                if row[i] == 0:
                    j = i
                    while j < end:
                        row[j], row[j+1] = row[j+1], row[j]
                        j += 1
                    end -=1
                else:
                    i += 1
        for row in self.grid:
            end = 3
            move_zeros(row)
            i = 0
            while i < end:
                if row[i] == row[i+1]:
                    row[i] *= 2
                    row[i+1] = 0
                    i += 2
                else:
                    i += 1
            move_zeros(row)


    def __add_value(self):
        result = np.where(self.grid == 0.)
        coordinates = list(zip(result[0], result[1]))
        random_coor = coordinates[np.random.randint(0,len(coordinates))]

        value = 4 if np.random.random() <= 0.1 else 2

        self.grid[random_coor[0]][random_coor[1]] = value

        self.score += value

    def __update(self):
        self.__save_grid()
        self.__add_value()
        self.__calculate_potential()
        self.__draw()

    def __draw(self):
        for i in self.grid:
            for j in i:
                if j == 0:
                    print('', end='\t')
                else:
                    print(j, end='\t')
            print("")
        print('')
        print(f"Score: {self.score}\tPotential: {self.potential}")

    def __wait_for_key(self):
        pass

    def __save_grid(self):
        pass


    def __calculate_potential(self):
        pass


    def __game_over(self):
        print("Game Over")

