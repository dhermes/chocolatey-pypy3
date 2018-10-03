# Investigating
# https://github.com/dhermes/ndb-rewrite/pull/12

import os
import sys


SEPARATOR = "=" * 60


def all3(name, value):
    print(SEPARATOR)
    print("{}:".format(name))
    print(type(value))
    print(value)
    print(repr(value))


def main():
    # size = os.get_terminal_size(sys.__stdout__.fileno())
    stdout = sys.__stdout__
    all3("stdout", stdout)

    fileno = stdout.fileno()
    all3("fileno", fileno)

    try:
        size = os.get_terminal_size(fileno)
        all3("size", size)
    except Exception as exc:
        all3("exc", exc)
        all3("exc.args", exc.args)


if __name__ == "__main__":
    main()
