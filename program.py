import game_code

import utill

# todo: add main()

utill.print_header('Guessing game')

player_name = input('Hello player what is your name? \n')
print(f'Hello {player_name} welcome to the game \n')
user_input_main_loop = 'EMPTY'
while user_input_main_loop != 'x' and user_input_main_loop:
    user_input_main_loop = input('[P]lay game, E[x]it: ')
    user_input_main_loop = user_input_main_loop.lower().strip()
    if user_input_main_loop == 'p':
        print('Starting Game \n')
        print('You have seven tries')
        game_code.guessing_game()
    elif user_input_main_loop == 'x' and user_input_main_loop:
        print('Thanks for playing')
