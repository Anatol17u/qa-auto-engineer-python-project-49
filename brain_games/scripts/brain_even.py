import random
import prompt

def parity_check():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if the number is even, otherwise answer "no".')
    winner_sum = 0 # фиксируем сумму побед
    while winner_sum < 3:
        number_questions = random.randint(1, 100)  # генерируем случайное число для вопроса
        correct_answer = 'yes' if number_questions % 2 == 0 else 'no'
        print(f'Question: {number_questions}')
        check = prompt.string('Your answer: ')
        if check == correct_answer:
            print('Correct!')
            winner_sum += 1
        else:
            winner_sum = 0
            print(f"'{check}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
    print(f'Congratulations, {name}!')

def main():
    parity_check()

if __name__ == "__main__":
    main()
