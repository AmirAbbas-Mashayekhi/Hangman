import random


class Hangman:
    def __init__(self, words: list):
        self.words = words
        self.guessed_letters = []
        self.lives = 6
        self.chosen_word = random.choice(words).lower()

    def display_in_terminal(self):
        for letter in self.chosen_word:
            if letter in self.guessed_letters:
                print(letter.upper(), end=' ')
            else:
                print('_', end=' ')
        print()

    def evaluate_user_guess(self):
        user_guess = input('Guess: ').lower()
        if user_guess == self.chosen_word:
            for letter in user_guess:
                self.guessed_letters.append(letter)
        elif user_guess in self.guessed_letters:
            print(f'Already Guessed {user_guess}')
        elif user_guess in self.chosen_word and user_guess != '':
            self.guessed_letters.append(user_guess)
        else:
            self.lives -= 1

    def won(self):
        return set(self.guessed_letters) == set(self.chosen_word)
