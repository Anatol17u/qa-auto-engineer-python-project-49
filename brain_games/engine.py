import prompt


def run_game(game_module):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")

    print(game_module.RULES)
    winner = 0
    while winner < 3:
        question, correct_answer = game_module.get_question_and_answer()
        print(f"Question: {question}")
        user_answer = prompt.string("Your answer: ")
        if user_answer == correct_answer:
            print("Correct!")
            winner += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
