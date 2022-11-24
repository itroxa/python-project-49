#!/usr/bin/env python3
import random


def show_rules():
    print("What is the result of the expression?")


def generate_question():
    operators = ('+', '-', '*')
    first_value = random.randint(1, 50)
    second_value = random.randint(1, 50)
    operation_sign = random.choice(operators)
    if operation_sign == '+':
        correct_answer = add(first_value, second_value)
    elif operation_sign == '-':
        correct_answer = sub(first_value, second_value)
    else:
        correct_answer = multiply(first_value, second_value)
    question = f"Question: {first_value} {operation_sign} {second_value}"
    return question, correct_answer


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False


def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def multiply(a, b):
    return a * b
