import random
from Cell import Cell


class Labyrinth:
    def __init__(self, height: int, length: int, difficulty_rating: int = 0):
        self.height = height
        self.length = length
        self.difficulty_rating = difficulty_rating

        # 2D-Liste von Zellen
        self.labyrinth: list[list[Cell]] = [
            [Cell(x, y) for x in range(length)] for y in range(height)
        ]

        self.start: Cell = None
        self.end: Cell = None

    def assign_neighbours(self):
        for y in range(self.height):
            for x in range(self.length):
                cell = self.labyrinth[y][x]

                # Nord
                if y > 0:
                    cell.add_neighbour(self.labyrinth[y - 1][x])
                # Süd
                if y < self.height - 1:
                    cell.add_neighbour(self.labyrinth[y + 1][x])
                # West
                if x > 0:
                    cell.add_neighbour(self.labyrinth[y][x - 1])
                # Ost
                if x < self.length - 1:
                    cell.add_neighbour(self.labyrinth[y][x + 1])

    def set_start(self, cell: Cell):
        self.start = cell

    def set_end(self, cell: Cell):
        self.end = cell

    def random_maze_generator(self):
        stack = [self.start]
        path = []
        self.start.visited = True

        while stack:
            cell = stack[-1]  # Peek at the top of the stack
            unvisited_neighbours = [n for n in cell.neighbours if not n.visited]

            if unvisited_neighbours:
                # Pick a random neighbor
                next_cell = random.choice(unvisited_neighbours)
                next_cell.visited = True

                # Remove walls between cell and next_cell
                dx = next_cell.x - cell.x
                dy = next_cell.y - cell.y
                if dx == 1:
                    cell.wall_east = False
                    next_cell.wall_west = False
                elif dx == -1:
                    cell.wall_west = False
                    next_cell.wall_east = False
                elif dy == 1:
                    cell.wall_south = False
                    next_cell.wall_north = False
                elif dy == -1:
                    cell.wall_north = False
                    next_cell.wall_south = False

                stack.append(next_cell)
                path.append(next_cell)
            else:
                stack.pop()  # Backtrack

        return path

    def generate_ascii_maze(self):
        maze_representation = []

        # Top border
        maze_representation.append("+" + "---+" * self.length)

        for y in range(self.height):
            # Row for cells and vertical walls
            row_cells = "|"
            row_walls = "+"
            for x in range(self.length):
                cell = self.labyrinth[y][x]

                # Cell space
                row_cells += "   "

                # Right wall
                row_cells += "|" if cell.wall_east else " "

                # Bottom wall
                row_walls += "---+" if cell.wall_south else "   +"

            maze_representation.append(row_cells)
            maze_representation.append(row_walls)

        return "\n".join(maze_representation)

    def __repr__(self):
        return f"Labyrinth({self.height}x{self.length}, difficulty={self.difficulty_rating})"
