import utill
# import game_code
import rpsmine
import os
import random


def main():
    utill.print_header('There is no internet and i am suffering')
    players = ['Player 1', 'Player 2']
    active_player_index = 0
    player = players[active_player_index]
    list_players(player, players)
    player_name = input('Hello player what is your name? \n')
    player = player_name
    print(player)
    list_players(player, players)
    print()
    user_input_main_loop = 'EMPTY'
    while user_input_main_loop != '3' and user_input_main_loop:
        user_input_main_loop = input(f'Hello {player} the chooses are (1)"play games","(3)EXIT"')
        user_input_main_loop = user_input_main_loop.lower().strip()
        if user_input_main_loop == "1":
            os.system("cls")
            print('loading')
            game_list()
        elif user_input_main_loop == '3' and user_input_main_loop:
            print('Thanks for playing')
    list_players(player, players)
    are_you_not_entertained()


# start under here


# print('The games are "(1)guess the number" and "(2)RPS" or go (3)back')


def end_it_all():
    pass


def let_the_games_begin():
    pass


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
    print('play again?')


def are_you_not_entertained():
    pass


def list_players(player, players):
    print()
    print(players)
    print(f'the current player is {player}')
    print()


def game_list():
    user_input_main_loop = 'EMPTY'
    while user_input_main_loop != '3' and user_input_main_loop:
        user_input_main_loop = input('The games are "(1)guess the number" and "(2)RPS" or go (3)back')
        user_input_main_loop = user_input_main_loop.lower().strip()
        if user_input_main_loop == '1':
            print('Starting Game \n')
            print('You have seven tries')
            guessing_game()
        elif user_input_main_loop == '2':
            print('Starting Game \n')
            player_1 = input('player 1 enter name\n')
            player_2 = 'computer'
            rpsmine.play_game(player_1, player_2)



        elif user_input_main_loop == '3' and user_input_main_loop:
            print('Thanks for playing')


# end here


if __name__ == '__main__':
    main()
