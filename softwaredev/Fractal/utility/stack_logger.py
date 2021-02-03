import sys
import logging

logging.basicConfig(filename='runtime-warnings.log',
					level=logging.WARNING,
					format='%(asctime)s %(message)s')

def log_stack(message):
    # Self report on frame stack
    f = sys._getframe()
    path = list()
    while True:
        try:
            f = f.f_back
            path.append(f.f_code.co_name)
        except:
            break

    stack = "->".join(reversed(path[:-1]))
    logging.warning(f"{stack} ({message})")

