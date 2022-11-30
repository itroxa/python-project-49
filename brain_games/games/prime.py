#!/usr/bin/env python3
import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def prime_check(number):
    for i in range(2, number):
        if (number % i) == 0:
            return "no"
    return "yes"


def qa_generate():
    number = random.randint(1, 100)
    question = f"Question: {number}"
    correct_answer = prime_check(number)
    return question, correct_answer
