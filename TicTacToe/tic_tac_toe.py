def print_board(board):
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board, player):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                      (0, 3, 6), (1, 4, 7), (2, 5, 8),
                      (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] == player:
            return True
    return False

def is_board_full(board):
    return all(cell in ['X', 'O'] for cell in board)

def main():
    board = [str(i) for i in range(1, 10)]
    current_player = "X"
    
    while True:
        print_board(board)
        move = input(f"Player {current_player}, choose your move (1-9): ")
        
        if not move.isdigit() or int(move) not in range(1, 10):
            print("Invalid input. Please choose a number between 1 and 9.")
            continue
        
        move = int(move) - 1
        
        if board[move] in ['X', 'O']:
            print("This spot is already taken. Choose another one.")
            continue
        
        board[move] = current_player
        
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        if is_board_full(board):
            print_board(board)
            print("It's a draw!")
            break
        
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
