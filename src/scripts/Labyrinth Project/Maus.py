class Maus:
    def __init__(self, x: int = 0, y: int = 0, goal_reached: bool = False):
        self.x = x
        self.y = y
        self.goal_reached = goal_reached

    def __repr__(self):
        return f"Maus(x={self.x}, y={self.y}, goal_reached={self.goal_reached})"