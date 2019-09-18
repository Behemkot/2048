import random

class Game2048:
    def __init__(self, demensions):
        self.demensions = demensions
        self.grid = []
        self.score = 0
        self.potential = 0
        self.__init_grid()
        self.__draw()


    def __init_grid(self):
        self.grid = [[None for x in range(self.demensions)] for y in range(self.demensions)]
        self.__add_value()
        self.__add_value()

    def up(self):
        pass
    def down(self):
        pass
    def right(self):
        # fliping grid verticaly
        for row in self.grid:
            for i in range(len(self.grid)/2):
                tmp = row[i]
                row[i] = row[-i]
                row[-i] = tmp



    def left(self):
        self.__motion()
        self.__update()



    def __motion(self):
        # remove None values
        clear_grid = [[x for x in row if x] for row in self.grid]
        new_grid = []
        for row in clear_grid:
            if len(row) >= 2:
                new_row = []
                i = 0
                pair = []
                while i < len(row):
                    if len(pair) != 2:
                        pair.append(row[i])
                        i+=1
                    else:
                        if pair[0] == pair[1]:
                            self.score += pair[0] + pair[1]
                            new_row.append(pair[0] + pair[1])
                            i+=1
                        else:
                            new_row.append(pair[0])
                            pair = list(pair[1])
                            i+=1
                new_grid.append(new_row)
            else:
                new_grid.append(row)

        for row in new_grid:
            while len(row) < self.demensions:
                row.append(None)

        self.grid = new_grid


    def __add_value(self):
        indeces = []

        for i in range(self.demensions):
            for j in range(self.demensions):
                if self.grid[i][j] == None:
                    indeces.append((i,j))

        if indeces:
            random_pair = random.sample(indeces, 1)
            random_pair = random_pair[0]
            value = 2

            if random.random() <= 0.1:
                value = 4
            self.score += value
            self.grid[random_pair[0]][random_pair[1]] = value
        else:
            self.__game_over()

    def __update(self):
        self.__save_grid()
        self.__add_value()
        self.__calculate_potential()
        self.__draw()

    def __draw(self):
        for i in self.grid:
            for j in i:
                print(j, end='\t')
            print("")
        print('')
        print(f"Score: {self.score}\tPotential: {self.potential}")



    def __save_grid(self):
        pass


    def __calculate_potential(self):
        pass


    def __game_over(self):
        print("Game Over")

