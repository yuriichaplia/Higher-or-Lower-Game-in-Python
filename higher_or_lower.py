import random
from game_data import data
from art import logo, vs

print(logo)

def people_choosing():
    return random.choice(data)

def checking(p_1, p_2):
    print(f"Compare A: {p_1['name']}, the {p_1['description']}, from {p_1['country']}")
    print(vs)
    print(f"Compare B: {p_2['name']}, the {p_2['description']}, from {p_2['country']}")

def compare(human1, human2, score, answer):
    if answer == 'a' and human1['follower_count'] > human2['follower_count']:
        score += 1
        print("\n" * 20)
        print(f"You're right. Current score: {score}")
    elif answer == 'a' and human1['follower_count'] < human2['follower_count']:
        print("\n" * 20)
        print(f"Sorry, that's wrong. Your score: {score}")
        exit()
    elif answer == 'b' and human1['follower_count'] < human2['follower_count']:
        score += 1
        print("\n" * 20)
        print(f"You're right. Current score: {score}")
    elif answer == 'b' and human1['follower_count'] > human2['follower_count']:
        print("\n" * 20)
        print(f"Sorry, that's wrong. Your score: {score}")
        exit()
    return score

def game():
    is_playing = True

    person1 = people_choosing()
    person2 = people_choosing()
    game_score = 0

    if person1 == person2:
        person2 = people_choosing()

    while is_playing:
        checking(person1, person2)

        user_input = input("Who has more followers? Type 'A' or 'B': ").lower()
        while user_input != 'a' and user_input != 'b':
            print("The answer should be 'A' or 'B' (does not matter if written in lowercase or uppercase).")
            user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

        if person1['follower_count'] > person2['follower_count']:
            person2 = people_choosing()

            if person1 == person2:
                person2 = people_choosing()

        elif person1["follower_count"] < person2["follower_count"]:
            person1 = person2
            person2 = people_choosing()

            if person1 == person2:
                person2 = people_choosing()

        game_score = compare(person1, person2, game_score, user_input)

game()