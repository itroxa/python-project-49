#!/usr/bin/env python3
import random


def show_rules():
    print("Find the greatest common divisor of given numbers.")


def generate_question():
    first_value = random.randint(1, 100)
    second_value = random.randint(1, 100)
    question = f"Question: {first_value} {second_value}"
    while first_value != second_value:
        if first_value > second_value:
            first_value = first_value - second_value
        else:
            second_value = second_value - first_value
    correct_answer = first_value
    return question, correct_answer


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False
