from enum import IntEnum


class GetOHLCDataInterval(IntEnum):
    VALUE_1 = 1
    VALUE_5 = 5
    VALUE_15 = 15
    VALUE_30 = 30
    VALUE_60 = 60
    VALUE_240 = 240
    VALUE_1440 = 1440
    VALUE_10080 = 10080
    VALUE_21600 = 21600

    def __str__(self) -> str:
        return str(self.value)
