#!/usr/bin/env python3
import random


def show_rules():
    print("Answer \"yes\" if given number is prime. Otherwise answer \"no\".")


def is_prime(number):
    divisor = 2
    if number > 1:
        while divisor < number / 2:
            if (number % divisor) == 0:
                return "no"
            divisor += 1
        return "yes"
    return "no"


def generate_question():
    number = random.randint(1, 100)
    question = f"Question: {number}"
    correct_answer = is_prime(number)
    return question, correct_answer


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False
