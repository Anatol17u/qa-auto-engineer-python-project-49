import random

RULES = 'What number is missing in the progression?'


def generate_parameters():
    start_number = random.randint(1, 20)
    step = random.randint(1, 10)
    range_number = random.randint(5, 10)
    return start_number, step, range_number


def currentElement(start, step, length):
    items = []
    for i in range(length):
        items.append(start + i * step)
    return items


def get_question_and_answer():
    start, step, length = generate_parameters()
    items = currentElement(start, step, length)
    random_index = random.randint(0, length - 1)
    correct_answer = str(items[random_index])
    for i in range(0, len(items)):
        items[i] = str(items[i])
    items[random_index] = '..'
    question = ' '.join(items)
    return question, correct_answer
