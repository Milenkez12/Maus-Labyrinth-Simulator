class Maus:
    __X_Cordinate: int = 0
    __Y_Cordinate: int = 0
    __Goalreached: bool = False

    # Getter und Setter für X_Cordinate
    @property
    def X_Cordinate(self) -> int:
        return self.__X_Cordinate

    @X_Cordinate.setter
    def X_Cordinate(self, value: int):
        self.__X_Cordinate = value

    # Getter und Setter für Y_Cordinate
    @property
    def Y_Cordinate(self) -> int:
        return self.__Y_Cordinate

    @Y_Cordinate.setter
    def Y_Cordinate(self, value: int):
        self.__Y_Cordinate = value

    # Getter und Setter für Goalreached
    @property
    def Goalreached(self) -> bool:
        return self.__Goalreached

    @Goalreached.setter
    def Goalreached(self, value: bool):
        self.__Goalreached = value