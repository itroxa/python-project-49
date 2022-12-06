#!/usr/bin/env python3
import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(number):
    return number % 2 == 0


def generate_qa():
    number = random.randint(1, 1000)
    question = f"Question: {number}"
    if is_even(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
