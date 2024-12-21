def create_game() -> dict:
    return {
        'board': [
            ['_', '|', '_', '|', '_'],
            ['_', '|', '_', '|', '_'],
            ['_', '|', '_', '|', '_'],
        ],
        'turn': 'X',
        'counter': 1
    }

def draw_board(game):
    print("  0   1   2")
    counter = 0
    for row in game['board']:
        print(counter, ' '.join(row))
        counter += 1
    print()

def input_square(game, x_or_o):
    while True:
        try:
            row, col = map(int, input(f'Enter {x_or_o}: ').split())
            actual_col = col * 2
            if 0 <= row <= 2 and 0 <= col <= 2:
                if game['board'][row][actual_col] == '_':
                    return row, actual_col
                else:
                    print("This place is already taken")
            else:
                print("The numbers must be between 0 - 2")
        except ValueError:
                print("enter two numbers separated by space")

def check_win(game, x_o: str) -> bool:
    for i in range(3):
        if all([game['board'][i][j] == x_o for j in range(3)]) or \
           all([game['board'][j][i] == x_o for j in range(3)]):
            return True
    if all([game['board'][i][i] == x_o for i in range(3)]) or \
       all([game['board'][i][2-i] == x_o for i in range(3)]):
        return True
    return False

def check_tie(game) -> bool:
    return game['counter'] >= 9


def play_x_o():
    my_game = create_game()

    while True:
        # X תור
        draw_board(my_game)
        row, col = input_square(my_game, 'X')
        my_game['board'][row][col] = 'X'
        my_game['counter'] += 1

        if check_win(my_game, 'X'):
            draw_board(my_game)
            print("X wins!")
            break

        if check_tie(my_game):
            draw_board(my_game)
            print("It's a tie!")
            break

        # 0 תור
        draw_board(my_game)
        row, col = input_square(my_game, 'O')
        my_game['board'][row][col] = 'O'
        my_game['counter'] += 1

        if check_win(my_game, 'O'):
            draw_board(my_game)
            print("O wins!")
            break

if __name__ == "__main__":
    play_x_o()