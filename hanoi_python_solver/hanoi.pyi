from poteau import Poteau
from typing import List, Tuple

class Hanoi:
    max_disk_number: int
    def __init__(self, nb_disks: int) -> None: ...
    def getABC(self) -> str: ...
    def move(self, t: Tuple[int, int]) -> bool: ...
    def possibleMoves(self) -> List[Tuple[int, int]]: ...
    def pathToSolution(self, solution: str) -> str: ...
    @property
    def getPoteau1(self) -> Poteau: ...
    @property
    def getPoteau2(self) -> Poteau: ...
    @property
    def getPoteau3(self) -> Poteau: ...
    @property
    def nbDisks(self) -> int: ...