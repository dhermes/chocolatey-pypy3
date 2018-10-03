# Investigating
# https://github.com/dhermes/ndb-rewrite/pull/12

import os
import sys


def main():
    # size = os.get_terminal_size(sys.__stdout__.fileno())
    stdout = sys.__stdout__
    print(stdout)
    fileno = stdout.fileno()
    print(fileno)
    size = os.get_terminal_size(fileno)
    print(size)


if __name__ == "__main__":
    main()
