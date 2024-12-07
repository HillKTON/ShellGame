from ._system_api import clear_screen
from ._numbers import NumbersGame


class GameMenu:
    def __init__(self):
        self.games = {"1": "Угадай число"}


    def main_menu(self):
        print("Доступный игры:")
        for index in self.games:
            print(f"{index}: {self.games[index]}")
        while True:
            user_input = input("Номер игры: >> ")
            match user_input:
                case "1":
                    numbers = NumbersGame()
                    numbers.run()
                case "exit":
                    break
                case _:
                    print("Неправильный индекс")


    def init(self):
        clear_screen()
        self.main_menu()
