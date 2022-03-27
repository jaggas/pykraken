from enum import Enum


class SystemStatus(str, Enum):
    ONLINE = "online"
    MAINTENANCE = "maintenance"
    CANCEL_ONLY = "cancel_only"
    POST_ONLY = "post_only"

    def __str__(self) -> str:
        return str(self.value)
