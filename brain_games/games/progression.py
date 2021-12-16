
import random
import prompt


# случайная арифметическая прогрессия
def ar_pr():
    start = random.randint(1, 10)
    step = random.randint(2, 20)
    length = random.randint(5, 10)
    stop = start + step * (length - 1)
    my_list = []
    for i in range(start, stop, step ):
        my_list.append(i)
    return my_list


def progression(name):
    print('What number is missing in the progression?')
    count = 0
    for _ in range(3):
        my_list = ar_pr()
        exclude = random.randint(0, len(my_list) - 1)
        num = my_list[exclude]
        my_list[exclude] = '..'
        print('Question:', end=' ')
        print(*my_list)
        ans = prompt.string('Your answer: ')
        if ans == str(num):
            print('Correct!')
            count += 1
        else:
            print("'{}' is wrong answer ;(.".format(ans), end=' ')
            print("Correct answer was '{}'".format(num))
            print("Let's try again, {}!".format(name))
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
