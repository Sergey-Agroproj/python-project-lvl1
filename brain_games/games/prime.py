
import random
import prompt


# проверяю простое число или составное
def prime(num):
    count = 0
    for i in range(1, num + 1):
        if num % i == 0:
            count += 1
    return count == 2


def is_prime(name):
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    for _ in range(3):
        num = random.randint(2, 100)
        print('Question:', num)
        ans = prompt.string('Your answer: ')
        if prime(num):
            may_ans = 'yes'
        else:
            may_ans = 'no'
        if ans == may_ans:
            print('Correct!')
            count += 1
        else:
            print("'{}' is wrong answer ;(.".format(ans), end=' ')
            print("Correct answer was '{}'".format(may_ans))
            print("Let's try again, {}!".format(name))
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
