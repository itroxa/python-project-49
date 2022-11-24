#!/usr/bin/env python3
import random


def show_rules():
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")


def generate_question():
    question_number = random.randint(1, 1000)
    if question_number % 2 == 0:
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return (question_number, correct_answer)


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False