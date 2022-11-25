#!/usr/bin/env python3
import prompt
import brain_games.cli
from brain_games.games.progression import show_rules, generate_question, check_answer


def game(rounds=3):
    print("Welcome to the Brain Games!")
    user_name = brain_games.cli.welcome_user()
    show_rules()
    round_counter = 0
    generate_question()
    while round_counter < rounds:
        question, correct_answer = generate_question()
        print(question)
        user_answer = prompt.integer("Your answer: ")
        check_result = check_answer(user_answer, correct_answer)
        if check_result:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")


def main():
    game()


if __name__ == '__main__':
    main()
