#!/usr/bin/env python3
import random
import prompt

def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False

def question():
    question_number = random.randint(1, 1000)
    if question_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (question_number, correct_answer)

def game(rounds=3):
    print("Welcome to the Brain Games!")
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    user_name = prompt.string("May I have your name? ")
    print(f"Hello, {user_name}!")
    round_counter = 0
    while round_counter < rounds:
        question_number, correct_answer = question()
        print(f"Question: {question_number}")
        user_answer = prompt.string("Your answer: ")
        check_result = check_answer(user_answer.lower().strip(), correct_answer)
        if check_result:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. Correct answer is '{correct_answer}'")
            print(f"Let's try again, {user_name}!")
            return
        if round_counter == rounds:
            print(f"Congratulations, {user_name}!")


def main():
    game()

if __name__ == '__main__':
    main()
