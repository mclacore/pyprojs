
# 1. Create a function that asks the user for a noun and returns the noun.

# 3. Print the paragraph to the screen.

# 4. Ask the user if they would like to play again. If they say yes, restart the game. If they say no, end the game.

def get_noun():
    noun = input("Enter a noun: ")
    return noun


def get_verb():
    verb = input("Enter a verb: ")
    return verb


def get_adjective():
    adjective = input("Enter an adjective: ")
    return adjective


def get_number():
    number = input("Enter a number: ")
    return number


def get_plural_noun():
    plural_noun = input("Enter a plural noun: ")
    return plural_noun


def get_body_part():
    body_part = input("Enter a body part: ")
    return body_part


def get_ing_verb():
    ing_verb = input("Enter a verb ending in 'ing': ")
    return ing_verb


def get_name():
    name = input("Enter a name: ")
    return name


def get_play_again():
    play_again = input("Would you like to play again? (y/n): ")
    return play_again


def get_paragraph():
    name = get_name()
    adjective = get_adjective()
    ing_verb = get_ing_verb()
    plural_noun = get_plural_noun()
    adjective = get_adjective()
    noun = get_noun()
    ing_verb = get_ing_verb()
    noun = get_noun()
    noun = get_noun()
    number = get_number()
    noun = get_noun()
    ing_verb = get_ing_verb()
    body_part = get_body_part()
    noun = get_noun()

    paragraph = f"Dr. {name} is a/an {adjective} surgeon. He specializes in {ing_verb}ing {plural_noun}. He is also a/an {adjective} {noun}. He is currently {ing_verb}ing a/an {noun} in {noun}. He has performed over {number} {noun}ectomys. Today, he will be {ing_verb}ing your {body_part} from your {noun}."
    return paragraph

def main():
    play_again = "y"
    while play_again == "y":
        paragraph = get_paragraph()
        print(paragraph)
        play_again = get_play_again()
        if play_again != "y":
            break
    print("Thanks for playing!")
