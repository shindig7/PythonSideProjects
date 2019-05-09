import numpy as np
from math import e
import logging

FORMAT = "[%(asctime)s] - [%(levelname)s] - [%(funcName)s] - %(message)s"
logging.basicConfig(level=10, format=FORMAT)

class NumberSet(object):
    def __init__(self, size):
        self.Size = size
        self.Revealed = []
        self.Hidden = [np.random.randint(1,1000000) for _ in range(self.Size)]
        self.Biggest = max(self.Hidden)

    def reveal(self):
        self.Revealed.append(self.Hidden.pop(0))


def play(set_size):
    num_set = NumberSet(set_size)
    stop_number = round(num_set.Size / e)
    final_guess = None
    for i in range(stop_number):
        num_set.reveal()
    top_guess = max(num_set.Revealed)
    for i in num_set.Hidden:
        if i > top_guess:
            final_guess = i
            #print("Final Guess: {}".format(final_guess))
            #print("Actual: {}\n".format(num_set.Biggest))
            if final_guess < num_set.Biggest:
                return False
            else:
                return True
            break
        else:
            continue
    if top_guess == num_set.Biggest:
        return False


def main():
    size = 10000000
    iterations = 10

    fail = 0
    success = 0
    logging.info("Begginning test with set_size={} and iterations={}".format(size, iterations))
    for i in range(iterations):
        ten_per = round(iterations/10)
        playthrough = play(size)
        if i % ten_per == 0:
            logging.info("{}% Complete".format((i / ten_per) * 10))
        if playthrough:
            success += 1
        else:
            fail += 1

    print("Success: {}".format(success))
    print("Fail: {}".format(fail))
    print("Ratio: {}%".format(round(success * 100 / iterations), 2))




if __name__ == "__main__":
    main()
