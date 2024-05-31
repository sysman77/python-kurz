import random

# Inicializace herního plánu
board = [' ' for _ in range(9)]

# Funkce pro zobrazení herního plánu
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |',)

# Funkce pro kontrolu, zda je pozice volná
def is_free(position):
    return board[position] == ' '

# Funkce pro kontrolu vítěze
def check_winner(board, player):
    win_cond = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                (0, 3, 6), (1, 4, 7), (2, 5, 8),
                (0, 4, 8), (2, 4, 6)]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_cond)

# Funkce pro kontrolu, zda je hra remíza
def is_draw(board):
    return ' ' not in board


# Funkce pro tah hráče
def player_move():
    position = int(input("Zadej pozici (1-9): ")) - 1
    if is_free(position):
        board[position] = 'X'
    else:
        print("Pozice je obsazená, zkus to znovu.")
        player_move()

# Funkce pro tah počítače
def computer_move():
    position = random.choice([i for i in range(9) if is_free(i)])
    board[position] = 'O'

# Hlavní smyčka hry
def main():
    print("Vítej ve hře Pískorky!")
    print_board(board)
    
    while True:
        player_move()
        print_board(board)
        if check_winner(board, 'X'):
            print("Gratulujeme, vyhrál jsi!")
            break
        if is_draw(board):
            print("Hra skončila remízou!")
            break
        
        computer_move()
        print_board(board)
        if check_winner(board, 'O'):
            print("Počítač vyhrál!")
            break
        if is_draw(board):
            print("Hra skončila remízou!")
            break

if __name__ == "__main__":
    main()

