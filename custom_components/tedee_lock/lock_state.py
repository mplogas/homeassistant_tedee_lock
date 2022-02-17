from enum import Enum, unique

@unique
class State(Enum):
    Unknown = 0
    Unlocked = 2
    HalfOpen = 3
    Unlocking = 4
    Locking = 5
    Locked = 6
    Pull = 7