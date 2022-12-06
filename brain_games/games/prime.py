#!/usr/bin/env python3
import random


GAME_RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for i in range(2, number):
        if (number % i) == 0:
            return False
    return True


def generate_qa():
    number = random.randint(1, 100)
    question = f"Question: {number}"
    if is_prime(number):
        correct_answer = "yes"
    else:
        correct_answer = "no"
    return question, correct_answer
