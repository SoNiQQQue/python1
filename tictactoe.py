import os
import random
import time


class Board:
    def __init__(self):
        self.cells = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def display(self):
        print("-------------")
        print("| {} | {} | {} |".format(self.cells[1], self.cells[2], self.cells[3]))
        print("-------------")
        print("| {} | {} | {} |".format(self.cells[4], self.cells[5], self.cells[6]))
        print("-------------")
        print("| {} | {} | {} |".format(self.cells[7], self.cells[8], self.cells[9]))
        print("-------------")

    def move(self, cell_number, player):
            self.cells[cell_number] = player

    def is_winner(self, player):
        for combination in [[1, 2, 3], [4, 5, 6], [7, 8, 9], [1, 4, 7], [2, 5, 8], [3, 6, 9], [1, 5, 9], [3, 5, 7]]:
            result = True
            for cell_number in combination:
                if self.cells[cell_number] != player:
                    result = False
            if result:
                return True
        return False

    def game_over(self): # если ничья
        crossed_cells = 0
        for cell in self.cells:
            if cell == "X" or cell == "O":
                crossed_cells += 1
        if crossed_cells == 9:
            return True
        else:
            return False

    def start_new_game(self):
        self.cells = []
        self.cells = [" ", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    def ai_move(self, player):
        """
        TODO: добавить проверку:
        может ли компьютер выиграть после хода
        может ли противник выиграть после хода (?????)
        есть ли свободный центр
        есть ли свободные углы
        """
        if self.cells[5] == "5":
                self.move(5, player)
        else:
            # Легкий уровень - случайный выбор ячейки
            num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            random.shuffle(num_list)
            for k in num_list:
                if self.cells[k] != "X" and self.cells[k] != "O":
                    self.move(k, player)
                    break


board = Board()


def refresh():
    os.system("clear")
    board.display()


def welcome():
    print("Поиграем? Выберите режим игры.")
    print("1 = Два игрока. Ходят по очереди.\n"
          "2 = Один игрок. За второго играет Мегамозг (бояться не стоит - он у нас еще маленький и глупенький).\n"
          "3 = Деморежим (за обоих игроков играет компьютер).\n"
          "0 = Выход из игры.")


welcome()
user_answer = input("\nВыберите 1, 2 или 3. >>> ")
if int(user_answer) == 1 or int(user_answer) == 2 or int(user_answer) == 3:
    print("\n==========================\n")
    print("Игра началась.\n"
          "Цель игры - быстрее противника закрыть три клетки в ряд по горизонтали, вертикали или диагонали.")

    refresh()

# TODO: перегруппировать ветвление
while True:

    if int(user_answer) == 1 or int(user_answer) == 2:
        while True:
            x_choice = input("\nХод первого игрока (X). Куда будем ходить? Укажите клетку от 1 до 9. >>> ")
            exit_game = False
            if 1 <= int(x_choice) <= 9 and board.cells[int(x_choice)] != "X" and board.cells[int(x_choice)] != "O":
                board.move(int(x_choice), "X")
                refresh()
                break
            elif int(x_choice) == 0:
                exit_game = True
                print("Вы вышли из игры. Жаль! А ведь все так хорошо начиналось...")
                break
            else:
                print("Такой ход невозможен, попробуйте еще раз.")
                continue
        if exit_game:
            break

    elif int(user_answer) == 3:
        print("Ход компьютера (играет за X). Компьютер думает...")
        time.sleep(random.randint(2, 10))
        board.ai_move("X")
        refresh()
    elif int(user_answer) == 0:
        print("\nМогли бы и не запускать программу, раз играть не хотите.")
        break
    else:
        print("Укажите 1, 2 или 3. Чтобы выйти, нажмите 0.")
        break

    if board.is_winner("X"):
        print("\nИгра окончена. Выиграл игрок Х.")
        rematch = input("Хотите сыграть еще раз? (Y/N) >>> ").upper()
        if rematch == "Y":
            board.start_new_game()
            continue
        else:
            print("Не хотите - как хотите")
            break
    if board.game_over():
        print("\nИгра окончена. В этот раз ничья.")
        rematch = input("Хотите сыграть еще раз? (Y/N) >>> ").upper()
        if rematch == "Y":
            board.start_new_game()
            continue
        else:
            print("Не хотите - как хотите!")
            break

    if int(user_answer) == 1:
        while True:
            exit_game = False
            o_choice = input("\nХод второго игрока (O). Куда будем ходить? Укажите клетку от 1 до 9. >>> ")
            if 1 <= int(o_choice) <= 9 and board.cells[int(o_choice)] != "X" and board.cells[int(o_choice)] != "O":
                board.move(int(o_choice), "O")
                refresh()
                break
            elif int(o_choice) == 0:
                exit_game = True
                print("Быстро вы наигрались! Ну да ладно, до скорого!")
                break
            else:
                print("Такой ход невозможен, попробуйте еще раз.")
                continue
        if exit_game:
            break

    elif int(user_answer) == 2 or int(user_answer) == 3:
        print("Ход компьютера (играет за O). Компьютер думает...")
        time.sleep(random.randint(2, 10))
        board.ai_move("O")
        refresh()
    else:
        print("Укажите 1, 2 или 3. Чтобы выйти, нажмите 0.")
        break

    if board.is_winner("O"):
        print("\nИгра окончена. Выиграл игрок O.")
        rematch = input("Хотите сыграть еще раз? (Y/N) >>> ").upper()
        if rematch == "Y":
            board.start_new_game()
            continue
        else:
            print("Не хотите - как хотите!")
            break
    if board.game_over():
        print("\nИгра окончена. В этот раз ничья.")
        rematch = input("Хотите сыграть еще раз? (Y/N) >>> ").upper()
        if rematch == "Y":
            board.start_new_game()
            continue
        else:
            print("Не хотите - как хотите!")
            break

