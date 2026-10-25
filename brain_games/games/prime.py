import random

RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_number(number):
    if number <= 1 or number % 2 == 0:
        return False
    elif number == 2:
        return True
    d = 3  
    while d * d <= number:
        if number % d == 0:
            return False
        d += 2   
    return True


def get_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_number(number) else 'no'
    return question, correct_answer
        
    



