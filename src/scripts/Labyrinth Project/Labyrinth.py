class Labyrinth:
    __height: int = 0
    __length: int = 0
    __difficulty_rating: int = 0
    labyrinth: list[list['Cell']] = []  # 2D-Array aus Cell-Objekten
    __start: 'Cell' = None
    __end: 'Cell' = None

    # Getter und Setter für Start
    @property
    def start(self) -> 'Cell':
        return self.__start

    @start.setter
    def start(self, value: 'Cell'):
        self.__start = value

    # Getter und Setter für End
    @property
    def end(self) -> 'Cell':
        return self.__end

    @end.setter
    def end(self, value: 'Cell'):
        self.__end = value
