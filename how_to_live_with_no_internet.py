import utill
import os
import random

rolls = {
    'rock': {
        'defeats': ['scissors'],
        'defeated_by': ['paper']
    },
    'paper': {
        'defeats': ['rock'],
        'defeated_by': ['scissors']
    },
    'scissors': {
        'defeats': ['paper'],
        'defeated_by': ['rock']
    },
}


def main():
    utill.print_header('There is no internet and i am suffering')
    players = ['Player 1', 'Player 2']
    active_player_index = 0
    player = players[active_player_index]
    # list_players(player, players)
    player_name = input('Hello player what is your name? \n')
    player = player_name
    # print(player)
    # list_players(player, players)
    first_choose(player, players)
    are_you_not_entertained()


# start under here

def first_choose(player, players):
    user_input_main_loop = 'EMPTY'
    while user_input_main_loop != '3':  # and user_input_main_loop:
        user_input_main_loop = input(f'Hello {player} the chooses are (1)"play games","(3)EXIT"')
        user_input_main_loop = user_input_main_loop.lower().strip()
        if user_input_main_loop == "1":
            os.system('cls')
            print('loading')
            game_list(player)
        elif user_input_main_loop == '3':  # and user_input_main_loop:
            print('Thanks for playing')
    list_players(player, players)


def end_it_all():
    pass


def let_the_games_begin():
    pass


def whole_rps(player):
    utill.print_header('Rock Paper Scissors')
    player_1 = player
    player_2 = 'computer'
    play_game(player_1, player_2)


def play_game(player_1, player_2):
    wins = {player_1: 0, player_2: 0}

    roll_names = list(rolls.keys())

    while not find_winner(wins, [player_1, player_2]):
        roll_1 = get_roll(player_1, roll_names)
        # roll_2 = get_roll(player_2, rolls)
        # player_2 = 'computer'
        roll_2 = random.choice(roll_names)

        if not roll_1:
            continue

        print(f'{player_1} rolls {roll_1}')
        print(f'{player_2} rolls {roll_2}')

        winner = check_for_winning_throw(player_1, player_2, roll_1, roll_2)

        if winner is None:
            print('this round was a tie!\n')
        else:
            print(f'{winner} takes the round!\n')
            wins[winner] += 1

        print(f'the score is {player_1}: {wins[player_1]} and {player_2}: {wins[player_2]}.\n')

    overall_winner = find_winner(wins, wins.keys())
    print(f'{overall_winner} wins the game!')


def find_winner(wins, names):
    best_of = 3
    for name in names:
        if wins.get(name, 0) >= best_of:  # try without the zero and see if it breaks
            return name


def check_for_winning_throw(player_1, player_2, roll_1, roll_2):
    winner = None
    if roll_1 == roll_2:
        print('you tied!')

    outcome = rolls.get(roll_1, {})
    if roll_2 in outcome.get('defeats'):
        return player_1
    elif roll_2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roll(player, roll_names):
    print("Available rolls:")
    for index, r in enumerate(roll_names, start=1):  # index is a variable
        print(f"{index}. {r}")

    text = input(f'\n{player} what is your roll?\n')
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print('do you even know what your doing? try again \n')
        return None

    return roll_names[selected_index]


def guessing_game(player):
    player_guess_num = -1
    the_number = random.randint(0, 100)
    # for player_guess_num in range(1, 7):
    # while player_guess_num != the_number:
    attempt_limit = 7
    attempts = 0

    while attempts < attempt_limit:
        try:
            player_guess_text = input(f'Hello {player} please enter a number between 1 and 100 \n')
            player_guess_num = int(player_guess_text)
            attempts += 1
            if player_guess_num > the_number:  # > greater then
                print(f'your guess of {player_guess_num} is too high')
            elif player_guess_num < the_number:  # < less then
                print(f'your guess of {player_guess_num} is to low')
            else:
                break
        except ValueError:
            print('please enter a number. ')
    if player_guess_num == the_number:
        print(f'correct! the number was {the_number}!')
        # print('Thanks for playing')
    else:
        print(f'\nNope. The Number I was thinking of was {the_number}\n')

    print(f'you took {attempts} guesses.\n')
    os.system('cls')
    print('play again?')


def are_you_not_entertained():
    pass


def list_players(player, players):
    print()
    print(players)
    print(f'the current player is {player}')
    print()


def game_list(player):
    user_input_main_loop = 'EMPTY'
    while user_input_main_loop != '3' and user_input_main_loop:
        user_input_main_loop = input('The games are "(1)guess the number" and "(2)RPS" or go (3)back')
        user_input_main_loop = user_input_main_loop.lower().strip()
        if user_input_main_loop == '1':
            os.system('cls')
            print('Starting Game \n')
            print('You have seven tries')
            guessing_game(player)
        elif user_input_main_loop == '2':
            print('Starting Game \n')
            player_1 = player
            player_2 = 'computer'
            play_game(player, player_2)
        elif user_input_main_loop == '3' and user_input_main_loop:
            print('Thanks for playing')


# end here


if __name__ == '__main__':
    main()
