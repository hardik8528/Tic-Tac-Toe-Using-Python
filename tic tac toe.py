# Genral Idea :=>

# Board
# Dispay Board
# Play Game
# Handel Turn
# Check Win => Check Rows, Check Column, Check diagonal
# Check Tie
# Flip Player

# -------------- Global Variable --------------------

# Game Board
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]


# If game is still going
game_still_going = True

# Who won ? Or Tie
winner = None

# Whose Turn is it
current_player = "X"


# Display Board
def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


# Play a game of tic tak tue
def play_game():

    # Display Initial Board
    display_board()

    # While the Game Is Still Going
    while game_still_going:

        # Handel a single turn of arbitarary player
        handel_turn(current_player)

        # Check if the game is ended
        check_if_game_over()

        # Flip to other player
        flip_player()

    # The game has ended
    if winner == "X" or winner == "O":
       print(winner + " won.")

    elif winner == None:
       print("Tie.")


# Handel a single turn of arbitarary player
def handel_turn(player):
    print(player + "'s Turn")
    position = input("Choose a Position From 1-9 :")

    valid = False
    while not valid:
      while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
        position = input("Choose a Position From 1-9 :")

      position = int(position) - 1

      if board[position] == "-":
         valid = True
      else :
         print("You cant go there , Go again")

    board[position] = player
    display_board()
    return


def check_if_game_over():
    check_for_winner()
    check_if_tie()
    return


def check_for_winner():

    # Set up global Variable
    global winner

    # Check Rows
    row_winner = check_rows()
    # Check Column
    column_winner = check_columns()
    # Check diagonal
    diagonal_winner = check_diagonals()

    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    return


def check_rows():

    # Set up global variablr
    global game_still_going

    # Ckeck if the any of row have all the same value (any is not empty)
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    # If any row match then there is winner
    if row_1 or row_2 or row_3:
        game_still_going = False

    # Return the winner (X or O)
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return


def check_columns():
    # Set up global variablr
    global game_still_going

    # Ckeck if the any of column have all the same value (any is not empty)
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    # If any column match then there is winner
    if column_1 or column_2 or column_3:
        game_still_going = False

    # Return the winner (X or O)
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_diagonals():
    # Set up global variablr
    global game_still_going

    # Ckeck if the any of column have all the same value (any is not empty)
    diagonals_1 = board[0] == board[4] == board[8] != "-"
    diagonals_2 = board[6] == board[4] == board[2] != "-"

    # If any column match then there is winner
    if diagonals_1 or diagonals_2:
        game_still_going = False

    # Return the winner (X or O)
    if diagonals_1:
        return board[0]
    elif diagonals_2:
        return board[6]
    return


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    # Global Variable 
    global current_player 
    
    # If current player is X then flip it to O
    if current_player == "X":
        current_player = 'O'

    # If current player is O then flip it to X
    elif current_player == "O":
        current_player = "X"
    return


play_game()
