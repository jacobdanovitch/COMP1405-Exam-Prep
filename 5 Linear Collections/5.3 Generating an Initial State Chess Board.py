def initboard():
    board = []
    for i in range(1,9):
        row = []
        if i == 1:
            row = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        elif i == 8:
            row = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        elif i == 2:
            row = ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P']
        elif i == 7:
            row = ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p']
        else:
            for j in range(1,9):
                row.append('-')
        board.append(row)

    for row in board:
        print(row)

    return board

initboard()
