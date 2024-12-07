import enum
from dataclasses import dataclass
from random import randint

from ._system_api import clear_screen


class Directions(enum.Enum):
    up = ("w", "2")
    down = ("s", "8")
    left = ("a", "4")
    right = ("d", "6")


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Memory:
    head: Coordinates
    point: Coordinates
    score: int


class XAdventureGame:
    def __init__(self):
        self.LIMITS = (9, 9)  # y, x
        self.memory = Memory(head=Coordinates(0, 0), point=Coordinates(0, 0), score=0)

    def printer(self, matrix: list[list[str]]) -> None:
        for row in matrix:
            print("  ".join(row))

    def move(self, vector: str) -> None:
        if vector.lower() in Directions.up.value:
            self.memory.head.y -= 1
        elif vector.lower() in Directions.down.value:
            self.memory.head.y += 1
        elif vector.lower() in Directions.left.value:
            self.memory.head.x -= 1
        elif vector.lower() in Directions.right.value:
            self.memory.head.x += 1

        self.move_validate()

    def move_validate(self) -> None:
        if self.memory.head.y < 0:
            self.memory.head.y = self.LIMITS[0]
        elif self.memory.head.y > self.LIMITS[0]:
            self.memory.head.y = 0

        if self.memory.head.x < 0:
            self.memory.head.x = self.LIMITS[1]
        elif self.memory.head.x > self.LIMITS[1]:
            self.memory.head.x = 0

    def point_generator(self, init: bool):
        if self.memory.head == self.memory.point:
            self.memory.point.x = randint(0, self.LIMITS[1])
            self.memory.point.y = randint(0, self.LIMITS[0])
            if not init:
                self.memory.score += 1

    def run(self):
        self.point_generator(init=True)
        while True:
            print(f"Head: {self.memory.head}")
            print(f"Score: {self.memory.score}")
            matrix = [["-" for _ in range(10)] for _ in range(10)]
            matrix[self.memory.head.y][self.memory.head.x] = "x"
            matrix[self.memory.point.y][self.memory.point.x] = "0"
            self.printer(matrix)
            userinput = input("Direction: >> ")
            if userinput.lower() == "exit":
                break
            else:
                self.move(userinput)
            self.point_generator(init=False)
            clear_screen()
