def criaJogoDamas(matBoard: 'list[list]'):
    tam_board = 12
    board = [['' for __ in range(tam_board)] for _ in range(tam_board)]
    for y in range(len(matBoard)):
        for x in range(0, len(matBoard[y])):
            if matBoard[y][x] == 0:
                board[y + 2][x + 2] = 'B'
            elif matBoard[y][x] == 1:
                board[y + 2][x + 2] = 'P'
            else:
                board[y + 2][x + 2] = ' '

    return {'campo': board}


def statusCasa(tad, y, x):
    board = tad['campo']
    if board[y][x] == '':
        return "Vazio"
    elif board[y][x] == 'P':
        return "Preto"
    else:
        return 'Branco'


def verficar_andar(tad, y: int, x: int) -> list:
    result = []
    board = tad['campo']
    print(board[y][x])
    if board[y][x] == 'B':
        if y + 1 in range(1, len(board) - 1) and x + 1 in range(1, len(board[0]) - 1) and board[y + 1][x + 1] == ' ':
            result.append([y + 1, x + 1])
        if y + 1 in range(1, len(board) - 1) and x - 1 in range(1, len(board[0]) - 1) and board[y + 1][x - 1] == ' ':
            result.append([y + 1, x - 1])
    elif board[y][x] == 'P':
        if y - 1 in range(1, len(board) - 1) and x + 1 in range(1, len(board[0]) - 1) and board[y - 1][x + 1] == ' ':
            result.append([y - 1, x + 1])
        if y - 1 in range(1, len(board) - 1) and x - 1 in range(1, len(board[0]) - 1) and board[y - 1][x - 1] == ' ':
            result.append([y - 1, x - 1])

    return result


def verificaComer(tad, y: int, x: int) -> 'list || False':
    result = []
    board = tad['campo']
    if board[y][x] == 'B':
        if y + 1 in range(1, len(board) - 1):
            if x in range(1, len(board[x]) - 1) and board[y + 1][x - 1] != board[y][x] and \
                    board[y + 1][x - 1] != ' ' and board[y + 2][x - 2] == ' ':
                result.append((y + 1, x - 1))
            if x in range(1, len(board[x]) - 1) and board[y + 1][x + 1] != board[y][x] and \
                    board[y + 1][x + 1] != ' ' and board[y + 2][x + 2] == ' ':
                result.append((y + 1, x + 1))

    elif board[y][x] == 'P':
        if y - 1 in range(1, len(board) - 1):

            if x - 1 in range(1, len(board[x]) - 1) and board[y - 1][x - 1] != board[y][x] and \
                    board[y - 1][x - 1] != ' ' and board[y - 2][x - 2] == ' ':
                result.append((y - 1, x - 1))
            if x + 1 in range(1, len(board[x]) - 1) and board[y - 1][x + 1] != board[y][x] and \
                    board[y - 1][x + 1] != ' ' and board[y - 2][x + 2] == ' ':
                result.append((y - 1, x + 1))
    return result


def posicionaPeca(tad, y, x, tipo):
    if y in range(1, len(tad['campo']) - 1) and x in range(1, len(tad['campo'][0]) - 1):
        if tipo == 1:
            tad['campo'][y][x] = 'P'
        elif tipo == 0:
            tad['campo'][y][x] = 'B'
        else:
            tad['campo'][y][x] = ' '


def toString(tad):
    board = tad['campo']
    str = '   '
    for i in range(1, len(board) - 1):
        str += f'   {i} '
    str += '\n'
    for y in range(1, len(board) - 1):
        str += f' {y} '
        for x in range(1, len(board) - 1):
            str += '| %2s ' % (board[y][x])

        str += f'|\n    {((len(board)) * "----")}\n'
    return str


def criaCampoInicial(tad):
    board = tad['campo']
    for y in range(1, len(board) - 1):
        for x in range(1, len(board[0]) - 1):
            if y < (len(board) - 1) // 2:
                if y % 2 == 0 and x % 2 != 0:
                    board[y][x] = 'B'
                elif y % 2 != 0 and x % 2 == 0:
                    board[y][x] = 'B'
            elif y >= (len(board) + 1) // 2:
                if y % 2 == 0 and x % 2 != 0:
                    board[y][x] = 'P'
                elif y % 2 != 0 and x % 2 == 0:
                    board[y][x] = 'P'
    tad['campo'] = board
    return tad


def main():
    board = [[-1 for _ in range(8)] for __ in range(8)]
    b = criaJogoDamas(board)
    criaCampoInicial(b)
    y, x = 6, 3
    posicionaPeca(b, y - 1, x - 1, 0)
    posicionaPeca(b, y - 2, x - 2, -1)
    posicionaPeca(b, y - 2, x, -1)
    print(toString(b))
    print(statusCasa(b, y, x))
    print(verficar_andar(b, y, x))
    print(verificaComer(b, y, x))


if __name__ == '__main__':
    main()
