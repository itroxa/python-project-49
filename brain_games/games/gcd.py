#!/usr/bin/env python3
import random


GAME_RULES = 'Find the greatest common divisor of given numbers.'


def gcd_check(first_value, second_value):
    while first_value != second_value:
        if first_value > second_value:
            first_value = first_value - second_value
        else:
            second_value = second_value - first_value
    return str(first_value)


def generate_qa():
    first_value = random.randint(1, 100)
    second_value = random.randint(1, 100)
    question = f"Question: {first_value} {second_value}"
    correct_answer = gcd_check(first_value, second_value)
    return question, correct_answer
