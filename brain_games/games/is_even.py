
import random
import prompt


def even(name):
    print('Answer "yes" if the number is even, otherwise "no".')
    count = 0
    for _ in range(3):
        request = random.randint(1, 100)
        print('Question: {}'.format(request))
        answer = prompt.string('Your answer: ')
        if request % 2 == 0:
            may_answer = 'yes'
        else:
            may_answer = 'no'
        if answer == may_answer:
            print('Correct!')
            count += 1
        else:
            print("""'{}' is wrong answer ;(. Correct answer was '{}'
Let's try again, {}!""".format(answer, may_answer, name))
            break
    if count == 3:
        print('Congratulations, {}!'.format(name))
