class Cell:
    def __init__(self, x: int, y: int, goal_reached: bool = False):
        self.x = x
        self.y = y
        self.goal_reached = goal_reached

        # Walls
        self.wall_north = False
        self.wall_south = False
        self.wall_east = False
        self.wall_west = False

        # Neighbours list (like ArrayList in Java)
        self.neighbours = []

    # Methods to manage neighbours
    def add_neighbour(self, neighbour):
        self.neighbours.append(neighbour)

    def remove_neighbour(self, neighbour):
        if neighbour in self.neighbours:
            self.neighbours.remove(neighbour)

    def __repr__(self):
        return f"Cell({self.x}, {self.y})"