from Cell import Cell

class Labyrinth:
    def __init__(self, height: int, length: int, difficulty_rating: int = 0):
        self.height = height
        self.length = length
        self.difficulty_rating = difficulty_rating

        # 2D list of Cell objects
        self.labyrinth: list[list[Cell]] = [
            [Cell(x, y) for x in range(length)] for y in range(height)
        ]

        # Start and end cells
        self.start: Cell = None
        self.end: Cell = None

    def set_start(self, cell: Cell):
        self.start = cell

    def set_end(self, cell: Cell):
        self.end = cell

    def random_maze_generator(self):
        # Depth-First Search algorithm will go here
        pass

    def __repr__(self):
        return f"Labyrinth({self.height}x{self.length}, difficulty={self.difficulty_rating})"