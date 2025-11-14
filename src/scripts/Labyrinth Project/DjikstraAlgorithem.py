from algorithm import Algorithm
from Cell import Cell

class DijkstraAlgorithm(Algorithm):
    def algorithmen(self, start: Cell, end: Cell) -> None:
        print(f"Dijkstra startet bei ({start.X_Cordinates}, {start.Y_Cordinates}) und endet bei ({end.X_Cordinates}, {end.Y_Cordinates})")