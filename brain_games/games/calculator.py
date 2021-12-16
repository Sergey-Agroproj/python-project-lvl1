
import random
import prompt


def calc(name):
    print('What is the result of the expression?')
    count = 0
    for _ in range(3):
        oper_list = ['+', '-', '*']
        a = random.randint(1, 10)
        b = random.randint(1, 10)
        c = random.choice(oper_list)
        result = eval(str(a) + c + str(b))
        print('Question: {} {} {}'.format(a, c, b))
        ans = prompt.string('Your answer: ')
        if ans == str(result):
            print('Correct!')
            count += 1
        else:
            print("'{}' is wrong answer ;(.".format(ans), end=' ')
            print("Correct answer was '{}'".format(result))
            print("Let's try again, {}!".format(name))
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
