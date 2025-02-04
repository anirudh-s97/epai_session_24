from enum import Enum, auto

class BookGenre(Enum):
    FICTION = auto()      # Will be 1
    NON_FICTION = auto()  # Will be 2
    SCIENCE = auto()      # Will be 3
    HISTORY = auto()      # Will be 4
    BIOGRAPHY = auto()    # Will be 5