from enum import Enum

class BaseLocators(Enum):
    def __str__(self):
        return str(self.value)