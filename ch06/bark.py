#!/usr/bin/env python

import os
from collections import OrderedDict

import commands


def print_bookmarks(bookmarks):
    for bookmark in bookmarks:
        print('\t'.join(
            str(field) if field else ''
            for field in bookmark
        ))


class Option:
    def __init__(self, name, command, prep_call=None):
        self.name = name  # <1>
        self.command = command  # <2>
        self.prep_call = prep_call  # <3>

    def _handle_message(self, message):
        if isinstance(message, list):
            print_bookmarks(message)
        else:
            print(message)

    def choose(self):  # <4>
        data = self.prep_call() if self.prep_call else None  # <5>
        message = self.command.execute(data) if data else self.command.execute()  # <6>
        self._handle_message(message)

    def __str__(self):  # <7>
        return self.name


def clear_screen():
    clear = 'cls' if os.name == 'nt' else 'clear'
    os.system(clear)


def print_options(options):
    for shortcut, option in options.items():
        print(f'({shortcut}) {option}')
    print()


def option_choice_is_valid(choice, options):
    return choice in options or choice.upper() in options  # <1>


def get_option_choice(options):
    choice = input('Choose an option: ')  # <2>
    while not option_choice_is_valid(choice, options):  # <3>
        print('Invalid choice')
        choice = input('Choose an option: ')
    return options[choice.upper()]  # <4>


def get_user_input(label, required=True):  # <1>
    value = input(f'{label}: ') or None  # <2>
    while required and not value:  # <3>
        value = input(f'{label}: ') or None
    return value


def get_new_bookmark_data():  # <4>
    return {
        'title': get_user_input('Title'),
        'url': get_user_input('URL'),
        'notes': get_user_input('Notes', required=False),  # <5>
    }


def get_bookmark_id_for_deletion():  # <6>
    return get_user_input('Enter a bookmark ID to delete')


def loop():  # <1>
    clear_screen()

    options = OrderedDict({
        'A': Option('Add a bookmark', commands.AddBookmarkCommand(), prep_call=get_new_bookmark_data),
        'B': Option('List bookmarks by date', commands.ListBookmarksCommand()),
        'T': Option('List bookmarks by title', commands.ListBookmarksCommand(order_by='title')),
        'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand(), prep_call=get_bookmark_id_for_deletion),
        'Q': Option('Quit', commands.QuitCommand()),
    })
    print_options(options)

    chosen_option = get_option_choice(options)
    clear_screen()
    chosen_option.choose()

    _ = input('Press ENTER to return to menu')  # <2>


if __name__ == '__main__':
    commands.CreateBookmarksTableCommand().execute()

    while True:  # <3>
        loop()


def for_listings_only():
    options = {
        'A': Option('Add a bookmark', commands.AddBookmarkCommand()),
        'B': Option('List bookmarks by date', commands.ListBookmarksCommand()),
        'T': Option('List bookmarks by title', commands.ListBookmarksCommand(order_by='title')),
        'D': Option('Delete a bookmark', commands.DeleteBookmarkCommand()),
        'Q': Option('Quit', commands.QuitCommand()),
    }
    print_options(options)
