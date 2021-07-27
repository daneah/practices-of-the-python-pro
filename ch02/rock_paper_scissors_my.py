# My implementation of the game.
import random

ROCK = 'rock'
PAPER = 'paper'
SCISSORS = 'scissors'

options = [ROCK, PAPER, SCISSORS]

DRAW = 'draw'
HUMAN = 'human'
COMPUTER = 'computer'
RESULT = [DRAW, HUMAN, COMPUTER]


def print_choice_message():
    """Prints choice message for the human."""
    
    options_with_numbers = [
        f'({num}) {opt}'for num, opt in enumerate(options, start=1)
    ]
    print('\n'.join(options_with_numbers))


def rule(h, c):
    """Rules of the game.

    Args:
        h (str): Human's choice.
        c (str): Computer's choice.

    Returns:
        str: The winnre of the game or a draw.

    """
    result = DRAW
    if h != c:
        if h == ROCK:
            result = COMPUTER if c == PAPER else HUMAN
        elif h == PAPER:
            result = COMPUTER if c == SCISSORS else HUMAN
        else:
            result = COMPUTER if c == ROCK else HUMAN

    return result


def print_result(winner, human_choice, computer_choice):
    """Prints the result of the game.

    Args:
        winner (str): Winner of the game.
        human_choice (str): Human's choice.
        computer_choice (str): Computer's choice.

    """
    result = 'Draw!'
    if winner != DRAW:
        if winner == HUMAN:
            result = f'Yes, {human_choice} beat {computer_choice}!'
        else:
            result = f'Sorry, {computer_choice} beat {human_choice}'
    
    print(result)


def do_human_choice():
    """Gets and prints the human choice.

    Returns:
        str: The human's choice.

    """
    human_choice = options[int(input('Enter the number of your choice: ')) - 1]
    print(f'You choice {human_choice}')

    return human_choice


def do_computer_choice():
    """Gets and prints the computer choice.

    Returns:
        str: The computers's choice.

    """
    computer_choice = random.choice(options)
    print(f'The computer choice {computer_choice}')

    return computer_choice


def start_game():
    print_choice_message()

    human_choice = do_human_choice()
    computer_choice = do_computer_choice()

    winner = rule(human_choice, computer_choice)

    print_result(winner, human_choice, computer_choice)


if __name__ == '__main__':
    start_game()
