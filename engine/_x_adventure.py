from dataclasses import dataclass

from ._system_api import clear_screen


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Memory:
    head: Coordinates


class XAdventureGame:
    def __init__(self):
        self.LIMITS = (9, 9)  # y, x

    def printer(self, matrix: list[list[str]]) -> None:
        for row in matrix:
            print("  ".join(row))

    def move(self, vector: str, memory: Memory) -> None:
        match vector:
            case "up":
                memory.head.y -= 1
            case "down":
                memory.head.y += 1
            case "left":
                memory.head.x -= 1
            case "right":
                memory.head.x += 1
        self.move_validate(memory)

    def move_validate(self, memory: Memory) -> None:
        if memory.head.y < 0:
            memory.head.y = self.LIMITS[0]
        elif memory.head.y > self.LIMITS[0]:
            memory.head.y = 0

        if memory.head.x < 0:
            memory.head.x = self.LIMITS[1]
        elif memory.head.x > self.LIMITS[1]:
            memory.head.x = 0

    def run(self):
        memory = Memory(head=Coordinates(0, 0))
        while True:
            print(f"Head: {memory.head}")
            matrix = [["-" for _ in range(10)] for _ in range(10)]
            matrix[memory.head.y][memory.head.x] = "x"
            self.printer(matrix)
            userinput = input("Direction: >> ")
            if userinput in ("w", "2"):
                self.move("up", memory)
            elif userinput in ("s", "8"):
                self.move("down", memory)
            elif userinput in ("a", "a"):
                self.move("left", memory)
            elif userinput in ("d", "6"):
                self.move("right", memory)
            elif userinput in ('exit', 'q'):
                break
            clear_screen()
