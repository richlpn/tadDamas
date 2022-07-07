def criaJogoDamas(matBoard: 'list[list]'):
    tam_board = 12
    board = [[-1 for __ in range(tam_board)] for _ in range(tam_board)]
    for y in range(len(matBoard)):
        for x in range(0, len(matBoard[y])):
            board[y + 2][x + 2] = matBoard[y][x]
    return {'campo': board}


def statusCasa(tad, y, x):
    y += 2
    x += 2
    board = tad['campo']
    if board[y][x] == -1:
        return "Vazio"
    elif board[y][x] == 1:
        return "Preto"
    else:
        return 'Branco'


def verficar_andar(tad, y: int, x: int) -> list:
    result = []
    board = tad['campo']
    if statusCasa(board, y, x) == 'branca':
        if board[y + 1][x] == -1:
            result = [y + 1, x]
    else:
        if board[y - 1][x] == -1:
            result = [y - 1, x]

    return result


def verificaComer(tad, y: int, x: int) -> 'list || False':
    result = []
    board = tad['campo']
    y += 2
    x += 2
    if board[y][x] == 0:
        if board[y + 1][x - 1] != board[y][x] and board[y + 1][x - 1] != -1 and board[y + 2][x - 2] == -1:
            result.append((y + 1, x - 1))
        if board[y + 1][x + 1] != board[y][x] and board[y + 1][x + 1] != -1 and board[y + 2][x + 2] == -1:
            result.append((y + 1, x + 1))

    elif board[y][x] == 1:
        if board[y - 1][x - 1] != board[y][x] and board[y - 1][x - 1] != -1 and board[y - 2][x - 2] == -1:
            result.append((y - 1, x - 1))
        if board[y - 1][x + 1] != board[y][x] and board[y - 1][x + 1] != -1 and board[y - 2][x + 2] == -1:
            result.append((y - 1, x + 1))
    return result


def print_board(tad):
    board = tad['campo']
    for y in range(1, len(board) - 1):
        for x in range(1, len(board) - 1):
            print('| %2i ' % (board[y][x]), end='')
        print('\n' + (len(board)) * '----')


def criaCampoIniciail(tad):
    board = tad['campo']
    for y in range(1, len(board) - 1):
        for x in range(1, len(board[0]) - 1):
            if y < (len(board) - 1) // 2:
                if y % 2 == 0 and x % 2 != 0:
                    board[y][x] = 0
                elif y % 2 != 0 and x % 2 == 0:
                    board[y][x] = 0
            elif y >= (len(board) + 1) // 2:
                if y % 2 == 0 and x % 2 != 0:
                    board[y][x] = 1
                elif y % 2 != 0 and x % 2 == 0:
                    board[y][x] = 1
    tad['campo'] = board
    return tad


if __name__ == '__main__':
    board = [[-1 for _ in range(8)] for __ in range(8)]
    b = criaJogoDamas(board)
    criaCampoIniciail(b)
    print_board(b)
    print(statusCasa(b, 1, 6))
    print(verificaComer(b, 2, 5))
