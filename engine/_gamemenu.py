from ._system_api import clear_screen
from ._numbers import NumbersGame
from ._x_adventure import XAdventureGame


class GameMenu:
    def __init__(self):
        self.games = {"1": "Угадай число", '2': 'X приключения'}

    def main_menu(self):
        print("Доступный игры:")
        for index in self.games:
            print(f"{index}: {self.games[index]}")
        while True:
            user_input = input("Номер игры: >> ")
            if user_input == "1":
                NumbersGame().run()
                break
            elif user_input == "2":
                XAdventureGame().run()
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
