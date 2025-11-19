import unittest
from Labyrinth import Labyrinth
from Cell import Cell

class Test:
    def test(self):
        labyrinth = Labyrinth(6, 6)
        labyrinth.set_start(labyrinth.labyrinth[0][3])
        labyrinth.set_end(labyrinth.labyrinth[5][5])
        labyrinth.simply_connected_maze()

        # Print the ASCII maze
        print(labyrinth.generate_ascii_maze())

if __name__ == "__main__":
    t = Test()
    t.test()