from abc import ABC, abstractmethod

# Interface (Abstract Base Class)
class Algorithms(ABC):
    @abstractmethod
    def algorithm(self, start: 'Cell', end: 'Cell') -> None:
        pass
