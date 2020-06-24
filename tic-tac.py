#!usr/bin/python3

class board:
    def __init__(self, *args, **kwargs):
        self.the_board = {
            'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' ',
        }
        self.possible_play = ['top-L', 'top-M', 'top-R',
                         'mid-L', 'mid-M', 'mid-R',
                         'low-L', 'low-M', 'low-R',]
        self.player = 'X'
        self.count = 9
        winner = ''
    
    def play(self, pos):
        if pos in self.possible_play:
            self.the_board[pos] = self.player
            self.possible_play.remove(pos)

            if self.player == 'X':
                self.player = 'O'
            else:
                self.player = 'X'

    def check(self):
        if self.the_board['top-L'] == self.the_board['top-M'] == self.the_board['top-R'] !=  ' ':
            self.winner = self.the_board['top-L']
        elif self.the_board['mid-L'] == self.the_board['mid-M'] == self.the_board['mid-R'] !=  ' ':
            self.winner = self.the_board['mid-L']
        elif self.the_board['low-L'] == self.the_board['low-M'] == self.the_board['low-R'] !=  ' ':
            self.winner = self.the_board['low-L']
        elif self.the_board['top-L'] == self.the_board['mid-L'] == self.the_board['low-L'] !=  ' ':
            self.winner = self.the_board['top-L']
        elif self.the_board['top-M'] == self.the_board['mid-M'] == self.the_board['low-M'] !=  ' ':
            self.winner = self.the_board['top-M']
        elif self.the_board['top-R'] == self.the_board['mid-R'] == self.the_board['low-R'] !=  ' ':
            self.winner = self.the_board['top-R']
        elif self.the_board['top-L'] == self.the_board['mid-M'] == self.the_board['low-R'] !=  ' ':
            self.winner = self.the_board['top-L']
        elif self.the_board['top-R'] == self.the_board['mid-M'] == self.the_board['low-L'] !=  ' ':
            self.winner = self.the_board['top-R']
        else:
            self.winner = ''
            return False
        return True


    def run(self):
        while (not self.check()) and self.count:
            self.display()
            print('Possible positions', ', '.join(self.possible_play))
            print(self.player, '\'s turn', sep='')
            myChoice = input('Pos: ')
            while myChoice not in self.possible_play:
                print('Invalid Input')
                print('Possible positions', ', '.join(self.possible_play))
                myChoice = input('Pos: ')
            self.count -= 1
            self.play(myChoice)
        self.display()
        if self.check:
            print('Winner is', self.winner)
        else:
            print('Draw!!!')
    
    def display(self):
        print('-'*13)
        print('| {} | {} | {} |'.format(self.the_board['top-L'],
                                self.the_board['top-M'],
                                self.the_board['top-R']))
        print('-'*13)
        print('| {} | {} | {} |'.format(self.the_board['mid-L'],
                                self.the_board['mid-M'],
                                self.the_board['mid-R']))
        print('-'*13)
        print('| {} | {} | {} |'.format(self.the_board['low-L'],
                                self.the_board['low-M'],
                                self.the_board['low-R']))
        print('-'*13)


if __name__ == '__main__':
    while True:
        app = board()
        app.run()
        again = input('Do you want to play again (Y/y to play again)').lower()
        if again == 'y':
            continue
        break