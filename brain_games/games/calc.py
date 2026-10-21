import random

RULES = 'What is the result of the expression?'


def get_question_and_answer():
    random_number_one = random.randint(1, 100)
    random_number_two = random.randint(1, 100)
    symbol = ['-', '+', '*']
    random_symbol = random.choice(symbol)
    if random_symbol == '-':
        correct_answer = random_number_one - random_number_two
    elif random_symbol == '+':
        correct_answer = random_number_one + random_number_two
    elif random_symbol == '*':
        correct_answer = random_number_one * random_number_two
    question = f'{random_number_one} {random_symbol} {random_number_two}'
    return question, str(correct_answer)

