from enum import Enum


class AddStandardOrderRequestBodyTimeinforce(str, Enum):
    GTC = "GTC"
    IOC = "IOC"
    GTD = "GTD"

    def __str__(self) -> str:
        return str(self.value)
