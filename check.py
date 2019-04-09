# Investigating
# https://github.com/dhermes/ndb-rewrite/pull/12

import ctypes
import nt
import os
import sys


SEPARATOR = "=" * 60


def all3(name, value):
    print(SEPARATOR)
    print("{}:".format(name))
    print(type(value))
    print(value)
    print(repr(value))


def get_by_id(exc_arg):
    # https://stackoverflow.com/a/15702647/1068170
    # This is looking for "<WindowsError object at 0x...>" in a string
    # and then trying to get the exception object from there.
    _, hex_val = exc_arg.split("<WindowsError object at 0x")
    hex_val, _ = hex_val.split(">", 1)
    all3("hex_val", hex_val)
    wrapped = ctypes.cast(int(hex_val, 16), ctypes.py_object)
    try:
        return wrapped.value
    except Exception as exc:
        return exc


def main():
    # size = os.get_terminal_size(sys.__stdout__.fileno())
    all3("nt", nt)

    stdout = sys.__stdout__
    all3("stdout", stdout)

    fileno = stdout.fileno()
    all3("fileno", fileno)

    # https://bitbucket.org/pypy/pypy/src/release-pypy3.5-v6.0.0/lib-python/3/os.py
    same = os.get_terminal_size is nt.get_terminal_size
    all3("same", same)

    try:
        size = os.get_terminal_size(fileno)
        all3("size", size)
    except Exception as exc:
        all3("exc", exc)
        all3("exc.args", exc.args)
        try:
            win_exc = get_by_id(exc.args[0])
            all3("win_exc", win_exc)
            all3("win_exc.__dict__", getattr(win_exc, "__dict__", None))
        except:
            pass

    try:
        size = os.get_terminal_size()
        all3("no args size", size)
    except Exception as exc:
        all3("no args exc", exc)
        all3("no args exc.args", exc.args)


if __name__ == "__main__":
    main()
