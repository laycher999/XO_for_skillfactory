board = list(range(1,10))
board1 = list(range(1,10))
player = 1

score_1 = 0
score_2 = 0

win = 1
draw = -1
run = 0
stop = 1

game = run

def draw_board():
    i = 1
    print('-' * 10)
    for n in range(3):
        while i <= 9:
            print(f'{board[i-1]} | {board[i]} | {board[i+1]}')
            print('-' * 10)
            i += 3

def checkpos(x):
    try:
        if board[x - 1] == x:
            return True
        else:
            print('Это место уже занято!')
            return False
    except:
        print('Введено неверное число')

def win_check():
    global game
    if board[0] == board[1] and board[1] == board[2] and board[0] != '1':
        game = win
    elif board[3] == board[4] and board[4] == board[5] and board[3] != '4':
        game = win
    elif board[6] == board[7] and board[7] == board[8] and board[6] != '7':
        game = win
    elif board[0] == board[3] and board[3] == board[6] and board[0] != '1':
        game = win
    elif board[1] == board[4] and board[4] == board[7] and board[1] != '2':
        game = win
    elif board[2] == board[5] and board[5] == board[8] and board[2] != '3':
        game = win
    elif board[0] == board[4] and board[4] == board[8] and board[4] != '5':
        game = win
    elif board[2] == board[4] and board[4] == board[6] and board[4] != '5':
        game = win
    elif board[0] != board1[0] and board[1] != board1[1] and board[2] != board1[2] and board[3] != board1[3] and board[4] != board1[4] and board[5] != board1[5] and board[6] != board1[6] and board[7] != board1[7] and board[8] != board1[8]:
        game = draw
    else:
        game = run

def continue_game():
    print(f'Счет {score_1}:{score_2}')
    input('Для продолжения игры нажмите ENTER')
    play_game()

def play_game():
    global player, board, game, score_1, score_2
    board = list(range(1,10))
    game = run
    while game == run:
        draw_board()
        if player % 2 != 0:
            print("Ход игрока 1")
            mark = 'X'
        else:
            print("Ход игрока 2")
            mark = 'O'
        choice = int(input(f'Выберите позицию для {mark}: '))
        if checkpos(choice):
            board[choice -1] = mark
            player += 1
            win_check()
        if game == draw:
            print("Ничья! Победила дружба!")
        elif game == win:
            player -= 1
            if player % 2 != 0:
                score_1 += 1
                print("Игрок 1 выиграл!")
            else:
                print("Игрок 2 выиграл!")
                score_2 += 1
    continue_game()

play_game()






