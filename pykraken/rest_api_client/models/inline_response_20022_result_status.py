from enum import Enum


class InlineResponse20022ResultStatus(str, Enum):
    QUEUED = "Queued"
    PROCESSING = "Processing"
    PROCESSED = "Processed"

    def __str__(self) -> str:
        return str(self.value)
