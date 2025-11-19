import unittest
from Perfect_Maze import Perfect_Maze
from Cell import Cell
from algorithm import Algorithm
from DFS import Depth_First_Search

class TestDFS(unittest.TestCase):
    def test_dfs_path(self):
        labyrinth = Perfect_Maze(6, 6)
        labyrinth.set_start(labyrinth.labyrinth[0][3])
        labyrinth.set_end(labyrinth.labyrinth[5][5])
        labyrinth.perfect_maze_generation()

        dfs_solver = Depth_First_Search()
        dfs_path = dfs_solver.algorithmen(labyrinth.start, labyrinth.end)

        # Print the ASCII maze
        print(labyrinth.generate_ascii_maze())
        print("DFS Path:", dfs_path)

        # Assert that path is not empty and ends at the correct cell
        self.assertTrue(len(dfs_path) > 0)
        self.assertEqual(dfs_path[-1], (labyrinth.end.x, labyrinth.end.y))

if __name__ == "__main__":
    unittest.main()