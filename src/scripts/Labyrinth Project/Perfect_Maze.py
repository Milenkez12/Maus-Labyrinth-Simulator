import random
from Cell import Cell


class Perfect_Maze:
    def __init__(self, height: int, length: int, difficulty_rating: int = 0):
        self.height = height
        self.length = length
        self.difficulty_rating = difficulty_rating

        # 2D-Liste von Zellen
        self.labyrinth: list[list[Cell]] = [
            [Cell(x, y) for x in range(length)] for y in range(height)
        ]

        self.start: Cell = self.labyrinth[0][0]
        self.end: Cell = self.labyrinth[length-1][height - 1]

    def which_maze(self,int = 0):
        if int == 0:
            self.perfect_maze_generation()
        elif int == 1:
            self.generate_ascii_maze()
        else:
            print("Invalid input")

    def imperfect_maze_generation(self):
        self.assign_neighbours()


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

    def perfect_maze_generation(self):
        self.assign_neighbours()
        stack = [self.start]
        path = []
        self.start.visited = True

        while stack:
            cell = stack[-1]
            unvisited_neighbours = [n for n in cell.neighbours if not n.visited]

            if unvisited_neighbours:
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
                stack.pop()

        # ✅ Open start and end
        self.start.wall_north = False
        self.end.wall_south = False
        self.neighbour_removal()

        return path

    def neighbour_removal(self):
        for y in range(self.height):
            for x in range(self.length):
                cell = self.labyrinth[y][x]

                # Check North
                if y > 0:
                    north = self.labyrinth[y - 1][x]
                    if cell.wall_north or north.wall_south:
                        cell.remove_neighbour(north)

                # Check South
                if y < self.height - 1:
                    south = self.labyrinth[y + 1][x]
                    if cell.wall_south or south.wall_north:
                        cell.remove_neighbour(south)

                # Check West
                if x > 0:
                    west = self.labyrinth[y][x - 1]
                    if cell.wall_west or west.wall_east:
                        cell.remove_neighbour(west)

                # Check East
                if x < self.length - 1:
                    east = self.labyrinth[y][x + 1]
                    if cell.wall_east or east.wall_west:
                        cell.remove_neighbour(east)

    def generate_ascii_maze(self):
        maze_representation = []

        # Top border: leave gap if start is open
        top_border = "+"
        for x in range(self.length):
            if self.labyrinth[0][x] == self.start and not self.start.wall_north:
                top_border += "   +"  # open entry
            else:
                top_border += "---+"
        maze_representation.append(top_border)

        for y in range(self.height):
            row_cells = "|"
            row_walls = "+"
            for x in range(self.length):
                cell = self.labyrinth[y][x]

                # Add S or E markers
                if cell == self.start:
                    row_cells += " S "
                elif cell == self.end:
                    row_cells += " E "
                else:
                    row_cells += "   "

                # Right wall
                row_cells += "|" if cell.wall_east else " "

                # Bottom wall
                if cell == self.end and not self.end.wall_south:
                    row_walls += "   +"  # open exit
                else:
                    row_walls += "---+" if cell.wall_south else "   +"

            maze_representation.append(row_cells)
            maze_representation.append(row_walls)

        return "\n".join(maze_representation)

    def __repr__(self):
        return f"Labyrinth({self.height}x{self.length}, difficulty={self.difficulty_rating})"
