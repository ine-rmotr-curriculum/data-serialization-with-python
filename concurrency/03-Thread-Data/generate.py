from random import sample, seed, randint
from string import ascii_letters
from time import time

def create_files(random_state=0):
    seed(random_state)
    for _files in range(1000):
        name = "".join(sample(ascii_letters, 5))
        with open(f"tmp-{name}.numbers", 'w') as fh:
            for _lines in range(20):
                print(randint(1, 99), file=fh)
    return time()

