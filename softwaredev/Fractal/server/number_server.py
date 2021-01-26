from threading import Thread
from queue import Queue
from time import sleep
from itertools import repeat, count, cycle
import gzip
from pickle import load
from os.path import join, dirname, abspath
from collections import namedtuple
from random import randrange

MOD_DIR = dirname(abspath(__file__))


def numbers(actions, sequence):
    instruction, gen = None, None
    while True:
        sleep(1e-6)   # wait a microsecond

        if not actions.empty():
            instruction = actions.get_nowait()

        if instruction is not None:
            if instruction.startswith('STOP'):
                break

            elif instruction.startswith('START'):
                _, seq_name = instruction.split()
                if seq_name == 'PRIMES':
                    gen = primes()
                elif seq_name == 'FIBONACCI':
                    gen = fibs()
                elif seq_name == 'NATURAL':
                    gen = count(1)
                elif seq_name == 'STOCHASTIC_INCREASING':
                    gen = stochastic_increasing()
                elif seq_name == 'STOCHASTIC_SLOW':
                    gen = stochastic_slow()
                else:
                    gen = repeat(0)

            elif instruction.startswith('FLUSH'):
                while not sequence.empty():
                    sequence.get()
                gen = None

            instruction = None

        while gen is not None and not sequence.full():
            sequence.put(next(gen))


def primes():
    # FIXME: implementation cycles through 1 million primes
    with gzip.open(join(MOD_DIR, 'primes.pkl.gz')) as fh:
        p1m = load(fh)
    yield from cycle(p1m)


def fibs():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b


def stochastic_increasing():
    for top in count(1):
        yield randrange(top)


def stochastic_slow():
    top = 2
    while True:
        n = randrange(top)
        yield n
        if n+1 == top:
            top += 1


class Server:
    def __init__(self, thread, actions, sequence):
        self._thread = thread
        self._actions = actions
        self._sequence = sequence

    def get(self, n=1):
        return [self._sequence.get() for _ in range(n)]
    
    def get_one(self):
        return self.get(n=1)[0]

    def command(self, cmd):
        self._actions.put(cmd)
        if cmd == 'STOP':
            self._thread = None
            self._sequence = None
            self._actions = None
        return self

    @property
    def n_ready(self):
        return self._sequence.qsize()


def make_server(queued=50):
    actions = Queue()
    sequence = Queue(maxsize=queued)
    thread = Thread(target=numbers,
                    name="Number server",
                    args=(actions, sequence))
    thread.start()
    return Server(thread, actions, sequence)

