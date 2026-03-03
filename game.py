import random

# Constants
GRID_SIZE = 3
EMPTY_TILE = ' '

# Initialize the game board
def initialize_board():
    board = [[0] * GRID_SIZE for _ in range(GRID_SIZE)]
    tiles = list(range(1, GRID_SIZE ** 2))
    random.shuffle(tiles)
    
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if tiles:
                board[i][j] = tiles.pop(0)
    return board

# Display the current game board
def display_board(board):
    for row in board:
        print("|", end=" ")
        for tile in row:
            if tile == 0:
                print(EMPTY_TILE, end=" | ")
            else:
                print(tile, end=" | ")
        print()

# Find the position of the empty tile (0)
def find_empty_tile(board):
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if board[i][j] == 0:
                return i, j
    return None

# Check if the game is won
def is_won(board):
    tiles = [board[i][j] for i in range(GRID_SIZE) for j in range(GRID_SIZE)]
    return tiles == list(range(1, GRID_SIZE ** 2)) + [0]

# Main game loop
def main():
    board = initialize_board()
    while True:
        display_board(board)
        if is_won(board):
            print("Congratulations! You solved the puzzle.")
            break
        empty_tile_position = find_empty_tile(board)
        if empty_tile_position is None:
            print("No valid moves left. The puzzle is unsolvable.")
            break
        row, col = empty_tile_position
        move = input("Enter a move (W/A/S/D to move, Q to quit): ").strip().upper()
        
        if move == 'Q':
            print("You quit the game.")
            break
        elif move == 'W' and row < GRID_SIZE - 1:
            board[row][col], board[row + 1][col] = board[row + 1][col], board[row][col]
        elif move == 'S' and row > 0:
            board[row][col], board[row - 1][col] = board[row - 1][col], board[row][col]
        elif move == 'A' and col < GRID_SIZE - 1:
            board[row][col], board[row][col + 1] = board[row][col + 1], board[row][col]
        elif move == 'D' and col > 0:
            board[row][col], board[row][col - 1] = board[row][col - 1], board[row][col]
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    main()