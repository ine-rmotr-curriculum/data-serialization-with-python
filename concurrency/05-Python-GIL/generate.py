from random import sample, seed, randint
from string import ascii_letters
from glob import glob
from os import remove

def create_files(random_state=0):
    [remove(fn) for fn in glob('tmp-*.numbers')]        
    seed(random_state)
    for _files in range(1000):
        name = "".join(sample(ascii_letters, 5))
        with open(f"tmp-{name}.numbers", 'w') as fh:
            for _lines in range(20):
                print(randint(1, 99), file=fh)

