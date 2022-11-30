#!/usr/bin/env python3
import operator
import random


GAME_RULES = 'What is the result of the expression?'


def calculate(first_value, second_value, operation_sign):
    if operation_sign == '+':
        return operator.add(first_value, second_value)
    elif operation_sign == '-':
        return operator.sub(first_value, second_value)
    else:
        return operator.mul(first_value, second_value)


def qa_generate():
    operators = ('+', '-', '*')
    first_value = random.randint(1, 50)
    second_value = random.randint(1, 50)
    operation_sign = random.choice(operators)
    correct_answer = str(calculate(first_value, second_value, operation_sign))
    question = f"Question: {first_value} {operation_sign} {second_value}"
    return question, correct_answer
