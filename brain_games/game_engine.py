#!/usr/bin/env python3
import prompt


ROUNDS = 3


def start_game(game_type):
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    print(game_type.GAME_RULES)
    round_counter = 0
    while round_counter < ROUNDS:
        question, correct_answer = game_type.qa_generate()
        print(question)
        user_answer = prompt.string("Your answer: ").lower()
        if user_answer == correct_answer:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")
