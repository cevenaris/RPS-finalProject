import random


class Board:
    def __init__(self, contents=[]):
        self.contents = contents

        if self.contents == []:
            self.contents = [' '] * 10

    def do_move(self, player_letter, location):
        self.contents[location] = player_letter

    def check_winner(self, player_letter):
        return ((self.contents[7] == player_letter and self.contents[8] == player_letter and self.contents
            [9] == player_letter) or  # across the top
                (self.contents[4] == player_letter and self.contents[5] == player_letter and self.contents
                    [6] == player_letter) or  # across the middle
                (self.contents[1] == player_letter and self.contents[2] == player_letter and self.contents
                    [3] == player_letter) or  # across the bottom
                (self.contents[7] == player_letter and self.contents[4] == player_letter and self.contents
                    [1] == player_letter) or  # down the left side
                (self.contents[8] == player_letter and self.contents[5] == player_letter and self.contents
                    [2] == player_letter) or  # down the middle
                (self.contents[9] == player_letter and self.contents[6] == player_letter and self.contents
                    [3] == player_letter) or  # down the right side
                (self.contents[7] == player_letter and self.contents[5] == player_letter and self.contents
                    [3] == player_letter) or  # diagonal
                (self.contents[9] == player_letter and self.contents[5] == player_letter and self.contents
                    [1] == player_letter))  # diagonal

    def clear_board(self):
        self.contents = [' '] * 10

    def print_board(self):
        print('   |   |')
        print(' ' + self.contents[7] + ' | ' + self.contents[8] + ' | ' + self.contents[9])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.contents[4] + ' | ' + self.contents[5] + ' | ' + self.contents[6])
        print('   |   |')
        print('-----------')
        print('   |   |')
        print(' ' + self.contents[1] + ' | ' + self.contents[2] + ' | ' + self.contents[3])
        print('   |   |')

    #    def get_copy(self):
    #       dupeBoard = Board(self.contents)

    def is_space_free(self, space):
        return self.contents[space] == ' '

    def get_free_spaces(self):
        pass

    def is_board_full(self):
        for i in range(1, len(self.contents) + 1):
            if self.is_space_free(i):
                return False
        return True

def assign_letters():
    letter = ''
    while not letter.upper() in ['X', 'O']:
        letter = input('Player 1, what letter would you like to be? ')

    if letter.upper() == 'X':
        return ['X', 'O']
    return ['O', 'X']


def who_goes_first():
    if random.randint(0, 1) == 0:
        return 1
    return 2

def choose_random_move(movesList):
    possibleMoves = []
    for i in movesList:
        if board.is_space_free(i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    return None


def computer_move(letters):
    for i in range(1, 10):
        copy = Board(board.contents)
        if copy.is_space_free(i):
            copy.do_move(letters[1], i)
            if copy.check_winner(letters[1]):
                return i

    for i in range(1, 10):
        copy = Board(board.contents)
        if copy.is_space_free(i):
            copy.do_move(letters[0], i)
            if copy.check_winner(letters[0]):
                return i

    move = choose_random_move([1, 3, 5, 7, 9])
    if move != None:
        return move

    if board.is_space_free(5):
        return 5

    return choose_random_move([2, 4, 6, 8])



def get_manual():
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not board.is_space_free(int(move)):
        move = input('Enter your next move (1-9): ')
    return int(move)

def play_again():
    again = input('Do you want to play again (y/[n])? ')
    return again.lower().startswith('y')


board = Board()
print('Welcome to the new and improved Tic Tac Toe!')
while True:
    board.clear_board()

    p2Manual = False
    p2 = input('Would you like to play against a friend (y/[n]? ')
    if p2.lower().startswith('y'):
        p2Manual = True
        print('Playing with 2 manual players.')
    else:
        print('You are playing against the computer.')

    letters = assign_letters()
    turn = who_goes_first()
    print('Player {}({}) is going first.'.format(turn, letters[turn - 1]))
    gamePlaying = True

    while gamePlaying:
        if turn == 1:
            board.print_board()
            print('Player 1({}) | '.format(letters[0]), end='')
            move = get_manual()
            board.do_move(letters[0], move)

            if board.check_winner(letters[0]):
                board.print_board()
                print('Player 1 won!')
                gamePlaying = False
            else:
                if board.is_board_full():
                    board.print_board()
                    print('The game is a tie!')
                    break
                else:
                    turn = 2

        elif turn == 2:
            if p2Manual == True:
                board.print_board()
                print('Player 2({}) | '.format(letters[1]), end='')
                move = get_manual()

            else:
                move = computer_move(letters)

            board.do_move(letters[1], move)

            if board.check_winner(letters[1]):
                board.print_board()
                print('Player 2 won!')
                gamePlaying = False
            elif board.is_board_full():
                board.print_board()
                print('The game is a tie!')
                break
            else:
                a = input('Paused.')
                turn = 1

    if not play_again():
        break

print('Thanks for playing!')

