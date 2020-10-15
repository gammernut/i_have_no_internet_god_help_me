import random


def guessing_game():
    player_guess_num = -1
    the_number = random.randint(0, 100)
    # for player_guess_num in range(1, 7):
    # while player_guess_num != the_number:
    attempt_limit = 7
    attempts = 0

    while attempts < attempt_limit:
        try:
            player_guess_text = input('please enter a number between 1 and 100 \n')
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
    print('play again?')

# much code very wow