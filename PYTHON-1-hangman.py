#!/usr/bin/env python3
"""Play hangman.

Essence of the code. Extra bits are in parenthesis:

The user is trying to guess letters in a string.
    (have a list of possible answers and have a random choice)
    (have a list of categories to choose from -- not implemented)
    (have option for a second player to enter the string -- not implemented)

The user only get a certain number of wrong guesses before they lose.

all unrevealed letters are represented by _ in the print out.

lets play:
-------------
user enters a letter
    (validate user entry)

if the guessed letter is in the string:
  re-print the string adding the newly revealed letters.
    (print preserving letter case)

if the guessed letter is not in the string:
  increment the total number of wrong guesses.
    (clear screen and print a hangman picture, depending on total # of wrong guesses.)

(print for user the right/wrong guesses for information)

determine if the game is won or lost and if so, print a message.
  win: if there are no more _
  lose: if the number of wrong answers reaches the limit. (# of hangman body parts.)

repeat.
"""
import sys
import os
import random


def validate_input(in_str, wrong_entries, right_entries):
    """Return T/F whether or not the input string is valid for this program, or exit.

    Parameters
    ----------
    in_str : str
        the user input string we are validating
    wrong_entries, right_entries : list of str
        lists containing lower case previous user input, e.g. ["a", "b", "c"]

    Returns
    -------
    bool
        True if the script can proceed with the given in_str
        False if the input is invalid and the user may try again.
        This function also exits the script if in_str = ""
    """
    # initial value, user has not input anything.
    if in_str is None:
        return False
    # Input value is blank for if the user wishes to exit:
    if in_str == "":
        print("User has exited")
        sys.exit(0)
    # Test if nput is not a letter:
    elif not in_str.isalpha():
        print("Input error: Please enter a letter only.")
        return False
    # Test if input is more than one letter:
    elif len(in_str) > 1:
        print("Input error: Please enter only one letter.")
        return False
    # Test if input has been before:
    elif in_str.lower() in wrong_entries + right_entries:
        print(
            "Input error: You have already guessed {}, please choose a different letter.".format(
                in_str
            )
        )
    else:
        return True


def fill_letter(letter, result, uncovered, right_entries, wrong_entries):
    """Fill in a hangman letter, or add the letter to wrong_entries array.

    This function will search `result` for `letter`. If it is found, those entries
    will be added to `uncovered` and letter added to `right_entries` array.
    If not found, letter will be added to `wrong_entries` array.

    Parameters
    ----------
    letter : str, or None
        The letter to search for. None means it will search for any non-alpha characters.
    result : string
        The hangman word or phrase we are guessing.
    uncovered : list of str
        This is a list containing the printed character for the turns. Meaning,
        each undiscovered letter in `result` will have a "_" entry in this list,
        and each discovered letter has that letter in this list. e.g. ["_","_","e"]
    right_entries, wrong_entries : list of str
        Lists containing the user guesses.
    """
    # Quick result: Check if letter is not None and also not in result.
    if (letter is not None) and (letter.lower() not in result.lower()):
        # append the letter to the wrong_entries array and exit function.
        wrong_entries.append(letter.lower())
        return
    elif letter is not None:
        # append the letter to the right_entries array
        right_entries.append(letter.lower())

    # If not above condition, we will need to go letter by letter:

    # loop over the indices from 0 to however long result is.
    # we can address both `result` and `uncovered` by this index.
    for i in range(len(result)):
        if letter is None:
            # This fills in all non-letter entries
            if not result[i].isalpha():
                uncovered[i] = result[i]
        else:
            # standardize everything to lower case:
            if letter.lower() == result[i].lower():
                # fill in the letter to uncovered:
                uncovered[i] = result[i]


def print_hangman(num_wrong):
    """Print the hangman.

    This function will take the first values from hangman_values and fill them in
    to the hangman picture. The rest of the values are replaced with spaces.
    """
    # These are the full list of hangman body parts that will be added, with escaped backslash.
    hangman_values = ["O", "/", "|", "\\", "|", "/", "\\"]

    # Create a way to extract the number of "lives" for the game.
    # This means we can change only this function to change how the hangman looks
    # and the number of "lives" we have.
    if num_wrong is None:
        return len(hangman_values)

    # the entries in the array `values` are the printed portion of hangman_values.
    # The entries in this array are spaces " ", unless the user has gotten wrong
    # answers.
    values = hangman_values[0:num_wrong] + [" "] * (len(hangman_values) - num_wrong)
    print("         + - - - - +")
    print("         |         |")
    print("         {}         |".format(values[0]))
    print("        {}{}{}        |".format(values[1], values[2], values[3]))
    print("         {}         |".format(values[4]))
    print("        {} {}        |".format(values[5], values[6]))
    print("                   |")
    print("     ______________|__")
    print("     ``````````````````")


def clear_and_print(uncovered, right_entries, wrong_entries):
    """Clear screen and print the hangman.

    This function clears the terminal, and prints the message before the
    user input prompt, including the hangman.
    """
    # I googled for this to find a way to clear the python screen.
    os.system("cls||clear")
    # print the header
    print("#######################")
    print("####### Hangman #######")
    print("#######################\n")
    print("Topic: Family Movies\n")

    # print the hangman
    print_hangman(len(wrong_entries))

    # print the phrase, either _ or the uncovered letter.
    print("\n{}\n".format(" ".join(uncovered)))

    # print the info list of right and wrong guesses.
    print("right letters:  {}".format(", ".join(right_entries)))
    print("wrong letters:  {}".format(", ".join(wrong_entries)))


# ###############################################################

# This list of movies was taken from IMBD editor's list of recommended family movies.
# I removed short ones, ones with many numbers, and ones with non-ascii characters.
potential_entries = [
    "The Mighty Ducks: Game Changers",
    "Spider-Man: Into the Spider-Verse",
    "Cobra Kai",
    "Matilda",
    "Wolfwalkers",
    "Ever After: A Cinderella Story",
    "Animaniacs",
    "Raya and the Last Dragon",
    "Missing Link",
    "The Mandalorian",
    "The Karate Kid",
    "Alex Rider",
    "Back to the Future",
    "Akeelah and the Bee",
    "Hunt for the Wilderpeople",
    "Bugsy Malone",
    "The Great Muppet Caper",
    "Paper Moon",
    "The Iron Giant",
    "School of Rock",
    "Hidden Figures",
    "The Book Thief",
    "To Kill a Mockingbird",
    "Stand and Deliver",
    "Osmosis Jones",
    "The Boy Who Harnessed the Wind",
    "Mr. Holland's Opus",
    "Earth at Night in Color",
    "Marvel Studios: Legends",
    "Earwig and the Witch",
    "Hamilton",
    "Onward",
]

# Use the random module to make a choice from potential guesses array. This is what
# we will try to uncover in the game.
result = random.choice(potential_entries)

# If there was any _ in the result, the puzzle won't be solveable.
# So: remove _ from result and replace with -
result = result.replace("_", "-")

# initialize some lists we will use to store user guesses
wrong_entries = []
right_entries = []

# array containing revealed letters, or _ for unguessed letters.
uncovered = ["_"] * len(result)

# call our print_hangman function to determine the number of "lives" the user has.
# our function is written so that this doesn't print anything, only gives us the
# number of hangman body parts.
num_lives = print_hangman(None)

# call fill_letter with letter=None, which will fill in all non-letter entries.
fill_letter(None, result, uncovered, right_entries, wrong_entries)

# clear screen and print the hangman
clear_and_print(uncovered, right_entries, wrong_entries)

# Repeat until win or lose:
while True:
    # Gather user input:

    # Set user input to none, and loop until vaild input is found.
    user_input = None
    while not validate_input(user_input, wrong_entries, right_entries):
        user_input = input("\nPlease enter a letter, or leave empty to exit program:  ")

    # fill input to appropriate right/wrong arrays and uncover if in result
    fill_letter(user_input.lower(), result, uncovered, right_entries, wrong_entries)

    # clear screen and print the hangman and updated clue.
    clear_and_print(uncovered, right_entries, wrong_entries)

    # Check if win or lose:
    # The win condition is when there is no more "_" left to uncover.
    if "_" not in uncovered:
        print("\n\n#######################")
        print("###### You win! #######")
        print("#######################")
        break

    # The lose condition is if the number of entries in wrong_entries is the
    # length of the hangman body parts array, hangman_values.
    if len(wrong_entries) == num_lives:
        msg = "You lose, the answer was: {}".format(result)

        print("\n\n" + "#" * len(msg))
        print(msg)
        print("#" * len(msg))
        break
