#!/usr/bin/env python3
import prompt
import brain_games.cli
import brain_games.games.calc


def game(rounds=3):
    print("Welcome to the Brain Games!")
    user_name = brain_games.cli.welcome_user()
    brain_games.games.calc.show_rules()
    round_counter = 0
    while round_counter < rounds:
        question, correct_answer = brain_games.games.calc.generate_question()
        print(question)
        user_answer = prompt.integer("Your answer: ")
        check_result = brain_games.games.calc.check_answer(user_answer, correct_answer)
        if check_result:
            print("Correct!")
            round_counter += 1
        else:
            print(f"'{user_answer}' is wrong answer ;(. "
                  f"Correct answer is '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
    print(f"Congratulations, {user_name}!")


def main():
    game()


if __name__ == '__main__':
    main()