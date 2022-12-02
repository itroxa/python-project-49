#!/usr/bin/env python3
import random

GAME_RULES = 'What number is missing in the progression?'


def generate_qa():
    elements_amount = 10
    start = random.randint(1, 50)
    step = random.randint(1, 50)
    end = start + step * elements_amount
    progression_list = list(range(start, end, step))
    element_to_remove = random.randint(0, elements_amount - 1)
    correct_answer = str(progression_list[element_to_remove])
    progression_list[element_to_remove] = ".."
    question = "Question: "
    for element in progression_list:
        question += str(element) + " "
    return question, correct_answer
