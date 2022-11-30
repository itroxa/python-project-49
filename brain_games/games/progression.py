#!/usr/bin/env python3
import random

GAME_RULES = 'What number is missing in the progression?'


def qa_generate():
    progression_elements = 10
    progression_start = random.randint(1, 50)
    progression_step = random.randint(1, 50)
    progression_end = progression_start \
        + progression_step \
        * progression_elements
    progression_list = list(range(progression_start,
                                  progression_end,
                                  progression_step))
    element_to_remove = random.randint(0, progression_elements - 1)
    correct_answer = str(progression_list[element_to_remove])
    progression_list[element_to_remove] = ".."
    question = "Question: "
    for element in progression_list:
        question += str(element) + " "
    return question, correct_answer
