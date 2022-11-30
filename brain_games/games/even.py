#!/usr/bin/env python3
import random


GAME_RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def parity_check(number):
    if number % 2 == 0:
        return "yes"
    else:
        return "no"


def qa_generate():
    number = random.randint(1, 1000)
    question = f"Question: {number}"
    correct_answer = parity_check(number)
    return question, correct_answer
