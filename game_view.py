class GameView:
    '''
    A game view for a two-player, sequential move, zero-sum,
    perfect-information game.
    '''

    def __init__(self, state, strategy):
        '''(GameView, GameState.__class__,
            Strategy.__class__) -> NoneType

        Create GameView self for game described by state, where
        computer uses given strategy.
        '''
        player = input('Type c if you wish the computer to play first ')
        if player == 'c':
            p = 'p2'
        else:
            p = 'p1'
            
        self.state = state(p, interactive=True)
        self.strategy = strategy(interactive=True)

    def play(self):
        ''' (GameView) -> NoneType

        Play a game.
        '''
        print(self.state.instructions)
        print(self.state + '\n')
        
        while self.state.possible_next_moves():
            if self.state.next_player == 'p1':
                m = self.state.get_move()
                while not m in self.state.possible_next_moves():
                    # The move was illegal.
                    print('Illegal move: {}\nPlease try again.\n'.format(m))
                    print(self.state.instructions)
                    print(self.state)
                    m = self.state.get_move()
                print('You choose: {}'.format(m))
            else:
                # The computer makes a move.
                m = self.strategy.suggest_move(self.state)
                print('The second computer chooses: {}'.format(m))
            self.state = self.state.apply_move(m)
            print('New game state: ', str(self.state))
            print()

        if self.state.winner('p2'):
            # p2, the computer, wins
            print('Beat ya!')
        elif self.state.winner('p1'):
            # p1, the human challenger, wins
            print('Congrats -- you won!!')
        else:
            print('We tied...')
            

if __name__ == '__main__':
    from subtract_square_state import SubtractSquareState
    from tippy_state import TippyState
    from tic_state import TicState

    game_state = ({'s': SubtractSquareState, 't': TippyState, 'tic':TicState})
    from strategy_random import StrategyRandom
    from strategy_minimax import StrategyMinimax

    strategy = ({'r': StrategyRandom, 'm': StrategyMinimax})
    g = ''
    while not g in game_state.keys():
        g = input('Choose s to play Subtract Square\n' +
                  'Choose t to play Tippy\n' +
                  'Choose tic to play TicTacToe\n')
    s = ''
    
    while not s in strategy.keys():
        s = input(
            'Choose r to play a computer with a random strategy.\n' +
            'Choose m to play a computer with the minimax strategy.\n')
        
    GameView(game_state[g], strategy[s]).play()
