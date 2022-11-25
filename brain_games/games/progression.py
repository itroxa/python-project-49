#!/usr/bin/env python3
import random


def show_rules():
    print("What number is missing in the progression?")


def generate_question():
    progression_elements = 10
    progression_start = random.randint(1, 25)
    progression_step = random.randint(1, 25)
    progression_end = progression_step * progression_elements
    progression_list = list(range(progression_start,
                                  progression_start + progression_end,
                                  progression_step))
    element_to_remove = random.randint(0, len(progression_list) - 1)
    correct_answer = progression_list[element_to_remove]
    progression_list[element_to_remove] = ".."
    question = "Question: "
    for element in progression_list:
        question += str(element) + " "
    return question, correct_answer


def check_answer(user_answer, correct_answer):
    if user_answer == correct_answer:
        return True
    else:
        return False
