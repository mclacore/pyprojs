
while True:
    name = input("Enter a name: ")
    adjective_1 = input("Enter an adjective: ")
    ing_verb_1 = input("Enter a verb ending in 'ing': ")
    plural_noun = input("Enter a plural noun: ")
    adjective_2 = input("Enter an adjective: ")
    noun_1 = input("Enter a noun: ")
    ing_verb_2 = input("Enter a verb ending in 'ing': ")
    noun_2 = input("Enter a noun: ")
    noun_3 = input("Enter a noun: ")
    number = input("Enter a number: ")
    noun_4 = input("Enter a noun: ")
    ing_verb_3 = input("Enter a verb ending in 'ing': ")
    body_part = input("Enter a body part: ")
    noun_5 = input("Enter a noun: ")


    print(f"Dr. {name} is a/an {adjective_1} surgeon. He specializes in {ing_verb_1} {plural_noun}. He is also a/an {adjective_2} {noun_1}. He is currently {ing_verb_2} a/an {noun_2} in {noun_3}. He has performed over {number} {noun_4}ectomys. Today, he will be {ing_verb_3} your {body_part} from your {noun_5}.")

    play_again = input("Would you like to play again? (y/n) ")
    if play_again.lower() != "y":
        break