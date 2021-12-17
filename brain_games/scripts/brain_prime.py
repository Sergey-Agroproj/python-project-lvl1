#!/usr/bin/env python


from brain_games.cli import welcome_user
from brain_games.games.prime import is_prime


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print('Hello, {}!'.format(name))

    is_prime(name)


if __name__ == '__main__':
    main()
