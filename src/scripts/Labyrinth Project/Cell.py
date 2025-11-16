class Cell:
    def __init__(self, x: int, y: int, goal_reached: bool = False):
        self.x = x
        self.y = y
        self.goal_reached = goal_reached

        # Walls
        self.wall_north = True
        self.wall_south = True
        self.wall_east = True
        self.wall_west = True

        # Neighbours list
        self.neighbours = []

        # Maze generation state
        self.visited = False  # <-- Add this line

    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def remove_neighbour(self, neighbour):
        if neighbour in self.neighbours:
            self.neighbours.remove(neighbour)

    def get_neighbour(self, index: int):
        if index < 0 or index >= len(self.neighbours):
            raise IndexError(f"Index {index} is out of range for neighbours list.")
        return self.neighbours[index]

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"