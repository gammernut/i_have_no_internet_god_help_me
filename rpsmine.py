import utill
import random
import how_to_live_with_no_internet

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
    utill.print_header('Rock Paper Scissors')
    player_1 = how_to_live_with_no_internet.main().player

    #player_1 = input('player 1 enter name\n')
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
            # print('really? its rock paper scissors not whatever the fuck that was\n')
            continue

        print(f'{player_1} rolls {roll_1}')
        print(f'{player_2} rolls {roll_2}')

        winner = check_for_winning_throw(player_1, player_2, roll_1, roll_2)

        # print('the game is over!')

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
        # winner = None
        print('you tied!')

    outcome = rolls.get(roll_1, {})
    # print(f"\n{roll_1} --> {outcome}'\n")
    if roll_2 in outcome.get('defeats'):
        return player_1
    elif roll_2 in outcome.get('defeated_by'):
        return player_2

    return winner


def get_roll(player_name, roll_names):
    print("Available rolls:")
    for index, r in enumerate(roll_names, start=1):  # index is a variable
        print(f"{index}. {r}")

    text = input(f'\n{player_name} what is your roll?\n')
    selected_index = int(text) - 1

    if selected_index < 0 or selected_index >= len(rolls):
        print('do you even know what your doing? try agene \n')
        return None

    return roll_names[selected_index]


if __name__ == '__main__':
    main()
