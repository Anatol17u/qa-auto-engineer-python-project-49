import random

RULES = 'Find the greatest common divisor of given numbers.'


def get_question_and_answer():
    number_one = random.randint(1, 100)
    number_two = random.randint(1, 100)
    question = f'{number_one} {number_two}'
    while number_two != 0:
        temp = number_two
        number_two = number_one % number_two
        number_one = temp
    correct_answer = number_one
    return question, str(correct_answer)
