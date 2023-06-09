#Author- Sami Gautam
#importing necessary codes
from noughtsandcrosses_2329843 import *

def main():
    #array list of values ,used as game board
    board = [ ['1','2','3'],\
              ['4','5','6'],\
              ['7','8','9']]

    #calling welcome function
    welcome(board)

    #total score is initialized as 0
    total_score = 0

    while True:
        #menu function returns choice (of user)
        choice = menu()
        if choice == '1':
            score = play_game(board)
            total_score += score
            print('Your current score is:',total_score)
        if choice == '2':
            save_score(total_score)
        if choice == '3':
            leader_board = load_scores()
            display_leaderboard(leader_board)
        if choice == 'q':
            print('Thank you for playing the "Unbeatable Noughts and Crosses" game.')
            print('Good-bye')
            return

# Program execution begins here
if __name__ == '__main__':
    main()