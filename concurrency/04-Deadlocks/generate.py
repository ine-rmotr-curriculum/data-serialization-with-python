from random import sample, seed, randint
from string import ascii_letters
from time import time
from glob import glob
import os

def create_files(random_state=0):
    [os.remove(fn) for fn in glob('tmp-*.numbers')]        
    names = []
    seed(random_state)
    for _files in range(50):
        name = "".join(sample(ascii_letters, 5))
        name = f"tmp-{name}.numbers"
        names.append(name)
        with open(name, 'w') as fh:
            for _lines in range(20):
                print(randint(1, 99), file=fh)
    return names

def operations(random_state=0):
    names = create_files(random_state)
    oplist = []
    seed(random_state)
    for n in range(1000):
        lineno = randint(1, 20)
        oplist.append([f"Line-{lineno}"] + sample(names, 3))
    return names, oplist

    