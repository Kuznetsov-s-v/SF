import random
#import os
#def cls():
#    os.system('cls' if os.name=='nt' else 'clear')
def two_game():
    player_one = input("Привет, это консольная игра - 'крестики нолики'\n"
                       "Учавствуют 2 игрока\n"
                       "Введите имя первого игрока: ")

    player_two = input("Введите имя второго игрока: ")

    print("перед вами поле 3х3,  для того что бы сделать ход, \n"
          "нужно ввести команду через пробел: поле по горизонтали(х) и по вертикали(у)\n"
          "например команда: '2 2' сделает ход в самом центре поля, а '2 3' правее.\n"
          "Игра начинается с крестика, далее первым ходит проигравший.")
    step_bool = True
    return player_one, player_two, step_bool
def new_game_field(N,M):
    # ввод матрицы
    A = [[" "] * M for i in range(N)]
    for i in range(N):
        for j in range(M - 3):
            A[i][j] = i
            A[j][i] = i
            A[0][0] = " "
    return A
def print_A(A):
    # вывод
    for row in A:  # делаем перебор всех строк матрицы A
        for elem in row:  # перебираем все элементы в строке row
            print(elem, end=' ')
        print()
def game(player_one,player_two,step_bool):
    if step_bool:
        print(player_one, " - твой ход")
        step_game_str = list(input("введи команду: ").split())
        while len(step_game_str) != 2:
            step_game_str = list(input("неверная команда, введи ещё раз: ").split())
        step_game = int(step_game_str[0]),int(step_game_str[1]), "X"
        step_bool = False
        #cls()
    else:
        print(player_two, " - твой ход")
        step_game_str = list(input("введи команду: ").split())
        while len(step_game_str) != 2:
            step_game_str = list(input("неверная команда, введи ещё раз: ").split())
        step_game = int(step_game_str[0]), int(step_game_str[1]), "0"
        step_bool = True
        #cls()
    return step_game, step_bool
def game_progress(step_game,step_bool,A,N,M,iter):
    for i in range(N):
        for j in range(M):
            if step_game[0] > 3 or step_game[0] < 1 or step_game[1] > 3 or step_game[1] < 1:
                print("Вышел за поле, попробуй еще раз")
                if step_bool:
                    step_bool = False
                else:
                    step_bool = True
                return step_bool, iter
            elif A[step_game[0]][step_game[1]] == " ":
                A[step_game[0]][step_game[1]] = step_game[2]
                print_A(A)
                iter += 1
                return step_bool,iter
            else:
                print("Клетка занята, пробуй еще раз")
                if step_bool:
                    step_bool = False
                else:
                    step_bool = True
                return step_bool,iter
def game_result(A,N,M,player_one, player_two, step_bool):
    for i in range(N):
        for j in range(M):
            if A[1][j] == A[2][j] == A[3][j]:
                if A[1][j]!=" ":
                    vicktory(A[1][j],player_one, player_two, step_bool)
            if A[i][1] == A[i][2] == A[i][3]:
                if A[i][1] != " ":
                    vicktory(A[i][1], player_one, player_two, step_bool)
            if A[1][1] == A[2][2] == A[3][3]:
                if A[1][1] != " ":
                    vicktory(A[1][1], player_one, player_two, step_bool)
            if A[1][3] == A[2][2] == A[3][1]:
                if A[1][3] != " ":
                    vicktory(A[i][1], player_one, player_two, step_bool)
def run():
    N = 4
    M = 4
    player_one, player_two, step_bool = two_game()
    A = new_game_field(N, M)
    print_A(A)
    iter = 0
    def run_requrce(player_one, player_two, step_bool,iter):
        if iter<((N-1)*(M-1)):
            step_game, step_bool = game(player_one, player_two, step_bool)
            step_bool,iter = game_progress(step_game,step_bool,A,N,M,iter)
            game_result(A,N,M,player_one, player_two, step_bool)
            run_requrce(player_one, player_two, step_bool,iter)
            return iter
        else:
            print("Конец игры! Ничья!")
            new_run(player_one, player_two, step_bool)
    run_requrce(player_one, player_two, step_bool,iter)
def new_run_two_go(player_one, player_two, step_bool):
    N = 4
    M = 4
    A = new_game_field(N, M)
    print_A(A)
    iter = 0
    def run_requrce(player_one, player_two, step_bool, iter):
        if iter < ((N - 1) * (M - 1)):
            step_game, step_bool = game(player_one, player_two, step_bool)
            step_bool, iter = game_progress(step_game, step_bool, A, N, M, iter)
            game_result(A, N, M,player_one, player_two, step_bool)
            run_requrce(player_one, player_two, step_bool, iter)
            return iter
        else:
            print("Конец игры! Ничья!")
            new_run(player_one, player_two, step_bool)
    run_requrce(player_one, player_two, step_bool, iter)
def new_run_one_go(player_one, player_two, step_bool):
    N = 4
    M = 4
    #player_one, player_two, step_bool = one_game()
    A = new_game_field(N, M)
    print_A(A)
    iter = 0
    def run_requrce(player_one, player_two, step_bool,iter):
        if iter<((N-1)*(M-1)):
            step_game, step_bool = game_one(player_one, player_two, step_bool,A,N,M)
            step_bool,iter = game_progress(step_game,step_bool,A,N,M,iter)
            game_result(A,N,M,player_one, player_two, step_bool)
            run_requrce(player_one, player_two, step_bool,iter)
            return iter
        else:
            print("Конец игры! Ничья!")
            new_run(player_one, player_two, step_bool)
    run_requrce(player_one, player_two, step_bool,iter)
def new_run(player_one, player_two, step_bool):
    new_run = input("Сыграем еще? введи 'Y'")
    if new_run == ("Y" or "y"):
        if id_hello:
            new_run_one_go(player_one, player_two, step_bool)
        else:
            new_run_two_go(player_one, player_two, step_bool)
        print("До встречи!")
        quit()
def vicktory(vick,player_one, player_two, step_bool):
    if vick == "X":
        print("Победа ", player_one)
    else:
        print("Победа ", player_two)
    new_run(player_one, player_two, step_bool)
def one_game():
    player_one = input("Привет, это консольная игра - 'крестики нолики'\n"
                       "Участвует 1 игрок\n"
                       "Введи имя: ")
    player_two = "Компьютер"

    print("перед вами поле 3х3,  для того что бы сделать ход, \n"
          "нужно ввести команду через пробел: поле по горизонтали(х) и по вертикали(у)\n"
          "например команда: '2 2' сделает ход в самом центре поля, а '2 3' правее.\n"
          "Игра начинается с крестика, далее первым ходит проигравший.")
    step_bool = True
    return player_one, player_two, step_bool
def game_one(player_one,player_two,step_bool,A,N,M):
    def comp_deserter(A,N,M):#Проверка возможной победы противника за один ход.
        for i in range(N):
            for j in range(M):
                if A[1][j] == A[2][j] == "X" or A[1][j] == A[3][j] == "X" or A[2][j] == A[3][j] == "X":
                    for i in A:
                        if i == " ": return int(step_game_str[i]), int(step_game_str[j]), "0"
                elif A[i][1] == A[i][2] == "X" or A[i][1] == A[i][3] == "X" or A[i][2] == A[i][3] == "X":
                    for i in A:
                        if i == " ": return int(step_game_str[i]), int(step_game_str[j]), "0"
                elif A[1][1] == A[2][2] == "X" and A[3][3] == " ":
                    return 3,3,"0"
                elif A[1][1] == A[3][3] == "X" and A[2][2] == " ":
                    return 2,2, "0"
                elif A[2][2] == A[3][3] == "X" and A[1][1] == " ":
                    return 1,1, "0"
                elif A[1][3] == A[2][2] == "X" and A[3][1] == " ":
                    return 3,1, "0"
                elif A[1][3] == A[3][1] == "X" and A[2][2] == " ":
                    return 2,2, "0"
                elif A[2][2] == A[3][1] == "X" and A[1][3] == " ":
                    return 1,3, "0"
                else:
                    step_game = random.randint(1, 3), random.randint(1, 3), "0"
                    if step_game[0] and step_game[1] != " ":
                        return step_game
    def comp_win(A,N,M): #проверка возможности победы
        for i in range(N):
            for j in range(M):
                if A[1][j] == A[2][j] != " " or A[1][j] == A[3][j] != " " or A[2][j] == A[3][j] != " ":
                    for i in A:
                        if i == " ": return i,j, "0"
                elif A[i][1] == A[i][2] != " " or A[i][1] == A[i][3] != " " or A[i][2] == A[i][3] != " ":
                    for i in A:
                        if i == " ": return i,j, "0"
                elif A[1][1] == A[2][2] != " " and A[3][3] == " ":
                    return 3,3, "0"
                elif A[1][1] == A[3][3] != " " and A[2][2] == " ":
                    return 2,2, "0"
                elif A[2][2] == A[3][3] != " " and A[1][1] == " ":
                    return 1,1, "0"
                elif A[1][3] == A[2][2] != " " and A[3][1] == " ":
                    return 3,1, "0"
                elif A[1][3] == A[3][1] != " " and A[2][2] == " ":
                    return 2,2, "0"
                elif A[2][2] == A[3][1] != " " and A[1][3] == " ":
                    return 1,3, "0"
                else:
                    return comp_deserter(A, N, M)
    if step_bool:
        print(player_one, " - твой ход")
        step_game_str = list(input("введи команду: ").split())
        while len(step_game_str) != 2:
            step_game_str = list(input("неверная команда, введи ещё раз: ").split())
        step_game = int(step_game_str[0]),int(step_game_str[1]), "X"
        step_bool = False
        #cls()
    else:
        print(player_two, " - мой ход")
        step_game = comp_win(A,N,M)
        step_bool = True
        #cls()
    return step_game, step_bool
def run_one():
    N = 4
    M = 4
    player_one, player_two, step_bool = one_game()
    A = new_game_field(N, M)
    print_A(A)
    iter = 0
    def run_requrce(player_one, player_two, step_bool,iter):
        if iter<((N-1)*(M-1)):
            step_game, step_bool = game_one(player_one, player_two, step_bool,A,N,M)
            step_bool,iter = game_progress(step_game,step_bool,A,N,M,iter)
            game_result(A,N,M,player_one, player_two, step_bool)
            run_requrce(player_one, player_two, step_bool,iter)
            return iter
        else:
            print("Конец игры! Ничья!")
            new_run(player_one, player_two, step_bool)
    run_requrce(player_one, player_two, step_bool,iter)
def hello():
    global id_hello
    print("Игра крестики-нолики\nBыбери режим: с компьютером - 1, вдвоем -2")
    player = input("Введи команду: ")
    if player == "1":
        id_hello = True
        run_one()
    elif player == "2":
        id_hello = False
        run()
    else:
        print("Не могу прочесть, попробуй еще раз")
        hello()
hello()