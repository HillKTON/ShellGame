from os import system as cmd
from time import sleep
from random import randint


def main():
    lc = input("Укажите число: ")
    if lc == "rnd":
        value = randint(0, 1000)
    else:
        value = int(lc)
    cmd("clear")
    arr = ["x", "x"]
    choice_count = 0
    while True:
        variant = input("Вариант: ")
        if variant == "/":
            print(f"Ответ: {value}")
            sleep(1)
            cmd("clear")
        else:
            try:
                choice_count += 1
                variant = int(variant)
                if variant > value:
                    if arr[1] != "x":
                        if variant > arr[1]:
                            pass
                        else:
                            arr[1] = variant
                    else:
                        arr[1] = variant
                    print(f"Меньше. {arr[0]} < x < {arr[1]} ")
                elif variant < value:
                    if arr[0] != "x":
                        if variant < arr[0]:
                            pass
                        else:
                            arr[0] = variant
                    else:
                        arr[0] = variant
                    print(f"Больше. {arr[0]} < x < {arr[1]}")
                elif variant == value:
                    print(f"Угадали! Попыток: {choice_count}")
                    break
                else:
                    raise ValueError("Jopa")
            except ValueError:
                print("Неверный вариант ответа!")

if __name__ == "__main__":
    playing = False
    while True:
        if playing:
            choice = input("Хотите сыграть ещё раз? [y, 0]: ")
            if choice in ("y", "0"):
                main()
            else:
                break
        else:
            playing = True
            main()
