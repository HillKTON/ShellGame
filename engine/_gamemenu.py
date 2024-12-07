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
            if user_input == "1":
                NumbersGame().run()
                break
            elif user_input == "exit":
                return "exit"
            else:
                print('Неверный индекс')

    def init(self):
        while True:
            clear_screen()
            status = self.main_menu()
            if status == "exit":
                break
