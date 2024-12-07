import enum
from dataclasses import dataclass
from random import randint, choices

from ._system_api import clear_screen


class Directions(enum.Enum):
    up = ("w", "2")
    down = ("s", "8")
    left = ("a", "4")
    right = ("d", "6")
    random_teleport = ("x", "5")


@dataclass
class Coordinates:
    x: int
    y: int


@dataclass
class Memory:
    head: Coordinates
    target: Coordinates
    special_target: bool
    score: int


class XAdventureGame:
    def __init__(self):
        self.LIMITS = Coordinates(x=12, y=12)
        self.memory = Memory(
            head=Coordinates(0, 0),
            target=Coordinates(0, 0),
            score=0,
            special_target=False,
        )

        self.SCREEN_SYMBOL = "."
        self.PLAYER_SYMBOL = "X"
        self.TARGET_SYMBOL = "0"
        self.SPECIAL_TARGET_SYMBOL = "%"

    def move(self, vector: str) -> None:
        if vector.lower() in Directions.up.value:
            self.memory.head.y -= 1
        elif vector.lower() in Directions.down.value:
            self.memory.head.y += 1
        elif vector.lower() in Directions.left.value:
            self.memory.head.x -= 1
        elif vector.lower() in Directions.right.value:
            self.memory.head.x += 1
        elif vector.lower() in Directions.random_teleport.value:
            self.player_random_teleport()

        self.move_validate()

    def player_random_teleport(self):
        self.memory.head.y = randint(0, self.LIMITS.x)
        self.memory.head.x = randint(0, self.LIMITS.x)

    def move_validate(self):
        if self.memory.head.y < 0:
            self.memory.head.y = self.LIMITS.y - 1
        elif self.memory.head.y == self.LIMITS.y:
            self.memory.head.y = 0

        if self.memory.head.x < 0:
            self.memory.head.x = self.LIMITS.x - 1
        elif self.memory.head.x == self.LIMITS.x:
            self.memory.head.x = 0

    def target_generator(self, init: bool):
        if self.memory.head == self.memory.target:
            if not self.memory.special_target:
                if not init:
                    self.memory.score += 1
                self.memory.special_target = choices((True, False), weights=(20, 80))[0]
                if not self.memory.special_target:
                    self.memory.target.y = randint(0, self.LIMITS.y - 1)
                    self.memory.target.x = randint(0, self.LIMITS.x - 1)
                else:
                    self.memory.target.y = randint(1, self.LIMITS.y - 2)
                    self.memory.target.x = randint(1, self.LIMITS.x - 2)
            else:
                self.memory.score += 10
                self.memory.special_target = False
                self.memory.target.y = randint(0, self.LIMITS.y - 1)
                self.memory.target.x = randint(0, self.LIMITS.x - 1)

    def screen_render(self):
        matrix = [
            [self.SCREEN_SYMBOL for _ in range(self.LIMITS.y)]
            for _ in range(self.LIMITS.x)
        ]

        if not self.memory.special_target:
            matrix[self.memory.target.y][self.memory.target.x] = self.TARGET_SYMBOL
        else:
            for i in range(-1, 2):
                for j in range(-1, 2):
                    y_cord = self.memory.target.y + i
                    x_cord = self.memory.target.x + j
                    if Coordinates(y=y_cord, x=x_cord) == self.memory.target:
                        matrix[y_cord][x_cord] = self.SPECIAL_TARGET_SYMBOL
                    else:
                        matrix[y_cord][x_cord] = self.TARGET_SYMBOL

        matrix[self.memory.head.y][self.memory.head.x] = self.PLAYER_SYMBOL

        for row in matrix:
            print("  ".join(row))

    def game_controls_view(self):
        print(f"\nКоординаты игрока: {self.memory.head}\nСчёт: {self.memory.score}")
        if self.memory.special_target:
            print(
                "Вам выпала особая цель! Соберите её центр, что-бы получить 10 очков!"
            )

        print(
            "\nУправление:\n"
            f"Вверх: {','.join(Directions.up.value)} | "
            f"Вниз: {','.join(Directions.down.value)} | "
            f"Лево: {','.join(Directions.left.value)} | "
            f"Право: {','.join(Directions.right.value)}\n"
            f"Случайная телепортация: {','.join(Directions.random_teleport.value)}"
        )

        print(
            "\nОбозначения:\n"
            f"Игрок: {self.PLAYER_SYMBOL} | "
            f"Цель: {self.TARGET_SYMBOL}"
        )

    def run(self):
        self.target_generator(init=True)
        while True:
            self.screen_render()
            self.game_controls_view()
            userinput = input("Направление: >> ")
            if userinput.lower() in ("q", "exit"):
                break
            else:
                self.move(userinput)
            self.target_generator(init=False)
            clear_screen()
