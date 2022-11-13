from game_data import data
import random

n = len(data) - 1
score = 0

if input("Do you wanna play [Y / N]: ").lower() == 'y':
    game = True
else:
    game = False


def higher_lower(user_choice, a_ig_followers, b_ig_followers):
    if user_choice == 'b' and a_ig_followers <= b_ig_followers:
        return True
    elif user_choice == 'a' and a_ig_followers >= b_ig_followers:
        return True
    else:
        return False


while game:
    a = random.randint(0, n)
    b = random.randint(0, n)

    while a == b:
        b = random.randint(0, n)

    dict_a = data[a]
    dict_b = data[b]

    print('Who has more IG followers?\n')
    print(f'Compare a: {dict_a["name"]}, a/an {dict_a["description"]}, from {dict_a["country"]}')
    print(f'Compare b: {dict_b["name"]}, a/an {dict_b["description"]}, from {dict_b["country"]}\n')

    b_ig_followers = dict_b["follower_count"]
    a_ig_followers = dict_a["follower_count"]

    # user guess
    user_choice = input('Choose between A and B: ').lower()
    if higher_lower(user_choice, a_ig_followers, b_ig_followers):
        game = True
        score += 1
        print(f'Your current score is {score}\n')
    else:
        print(f'You lost with score {score}\n')
        print('GAME OVER')
        game = False


