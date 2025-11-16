import unittest
from Labyrinth import Labyrinth
from Cell import Cell

class Test:
    def test(self):
        labyrinth = Labyrinth(10, 10)
        labyrinth.assign_neighbours()
        labyrinth.set_start(labyrinth.labyrinth[0][0])
        labyrinth.set_end(labyrinth.labyrinth[4][4])
        labyrinth.random_maze_generator()

        # Print the ASCII maze
        print(labyrinth.generate_ascii_maze())

if __name__ == "__main__":
    t = Test()
    t.test()