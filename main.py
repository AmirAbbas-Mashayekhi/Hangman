from hangman import Hangman

words = ['amir', 'hangman', 'gamer', 'Computer', 'Python']
game = Hangman(words)

while game.lives > 0 and not game.won():
    game.display_in_terminal()
    game.evaluate_user_guess()
    print(f"Remaining lives: {game.lives}")

if game.won():
    print("Congratulations, You've won!")
else:
    print("You lost.")
print(f"the word was: {game.chosen_word}")
