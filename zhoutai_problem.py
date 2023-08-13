import random
import numpy as np

expectation = 0
probality = []
probality.append(1)
for i in range(1, 13):
    probality.append(probality[i-1] * (13 - i) / 13.0)
    expectation += i * (probality[i-1] - probality[i])
print(expectation + probality[12] * 13)


def rounds_of_zhoutai():
    cards = []
    rounds = 1
    cards.append(np.random.randint(1, 14))
    for k in range(1, 13):
        number = np.random.randint(1, 14)
        if number in cards:
            break
        else:
            cards.append(number)
            rounds += 1
    return rounds


for i in range(20):
    list = []
    for _ in range(10000):
        list.append(rounds_of_zhoutai())
    print(sum(list) / 10000)



