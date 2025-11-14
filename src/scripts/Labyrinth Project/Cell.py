class Cell:

    __X_Cordinates: int = 0
    __Y_Cordinates: int = 0
    __Wall_North: bool = False
    __Wall_South: bool = False
    __Wall_East: bool = False
    __Wall_West: bool = False

    @property
    def X_Cordinates(self) -> int:
        return self.__X_Cordinates

    @X_Cordinates.setter
    def X_Cordinates(self, value: int):
        self.__X_Cordinates = value

    # Getter und Setter für Y_Cordinates
    @property
    def Y_Cordinates(self) -> int:
        return self.__Y_Cordinates

    @Y_Cordinates.setter
    def Y_Cordinates(self, value: int):
        self.__Y_Cordinates = value

    @property
    def Wall_North(self) -> bool:
        return self.__Wall_North

    @Wall_North.setter
    def Wall_North(self, value: bool):
        self.__Wall_North = value