
import random
import prompt


def is_even(name):
    print('Answer "yes" if the number is even, otherwise "no".')
    count = 0
    for _ in range(3):
        req = random.randint(1, 100)
        print('Question: {}'.format(req))
        ans = prompt.string('Your answer: ')
        if req % 2 == 0 and ans == 'yes' or req % 2 == 1 and ans == 'no':
            print('Correct!')
            count += 1
        else:
            if req % 2 == 0:
                may_ans = 'yes'
            if req % 2 == 1:
                may_ans = 'no'
            print("'{}' is wrong answer ;(.".format(ans), end=' ')
            print("Correct answer was '{}'".format(may_ans))
            print("Let's try again, {}!".format(name))
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
