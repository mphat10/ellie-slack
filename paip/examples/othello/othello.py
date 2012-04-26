from paip import othello

def check(move, player, board):
    return othello.is_valid(move) and othello.is_legal(move, player, board)

def human(player, board):
    print othello.print_board(board)
    print 'Your move?'
    while True:
        move = raw_input('> ')
        if move and check(int(move), player, board):
            return int(move)
        elif move:
            print 'Illegal move--try again.'

def get_choice(prompt, options):
    print prompt
    print 'Options:', options.keys()
    while True:
        choice = raw_input('> ')
        if choice in options:
            return options[choice]
        elif choice:
            print 'Invalid choice.'

def get_players():
    print 'Welcome to OTHELLO!'
    options = { 'human': human,
                'random': othello.random_strategy,
                'max-diff': othello.max_difference,
                'max-weighted-diff': othello.max_weighted_difference }
    black = get_choice('BLACK: human or computer?', options)
    white = get_choice('WHITE: human or computer?', options)
    return black, white

def main():
    black, white = get_players()
    try:
        board, score = othello.play(black, white)
    except othello.IllegalMoveError as e:
        print e
        return
    print 'Final score:', score
    print '%s wins!' % ('Black' if score > 0 else 'White')
    print othello.print_board(board)
