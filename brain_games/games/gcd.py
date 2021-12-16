
import random
import prompt


# функция нахождения НОД двух чисел
def max_cd(a, b):
    temp = 0
    while b != 0:
        temp = b
        b = a % b
        a = temp
    return a


def is_gcd(name):
    print('Find the greatest common divisor of given numbers.')
    count = 0
    for _ in range(3):
        req_1 = random.randint(1, 10)
        req_2 = random.randint(1, 10)
        print('Question: {} {}'.format(req_1, req_2))
        ans = prompt.string('Your answer: ')
        if ans == str(max_cd(req_1, req_2)):
            print('Correct!')
            count += 1
        else:
            print("'{}' is wrong answer ;(.".format(ans), end=' ')
            print("Correct answer was '{}'".format(max_cd(req_1, req_2)))
            print("Let's try again, {}!".format(name))
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
