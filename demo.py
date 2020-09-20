# encoding: UTF-8

import os, io
from strategy_platform.api import (second_timer)


def test_builtin_open(*args, **kwargs):
    filename = kwargs["filename"]
    f = open(filename, 'w+')
    f.write("111")
    f.close()

    f = open(filename, 'w')
    seq = ['11111']
    f.writelines(seq)
    f.close()

    f = open(filename)
    print(f.read())
    f.close()

    f = open(filename)
    print(f.read(3))
    f.close()

    f = open(filename)
    print(f.readline())
    f.close()

    f = open(filename)
    print(f.readline(2))
    f.close()

    f = open(filename)
    print(f.readlines())
    f.close()


def test_os_open(*args, **kwargs):
    filename = kwargs["filename"]
    f = os.open(filename, os.O_RDWR| os.O_CREAT)
    os.write(f, "2222".encode())
    os.close(f)

    f = os.open(filename, os.O_RDONLY)
    print(os.read(f, 100))
    os.close(f)


def test_io_open(*args, **kwargs):
    filename = kwargs["filename"]
    f = io.open(filename, 'w+')
    f.write(u"333")
    f.close()

    f = open(filename, 'w')
    seq = [u"333"]
    f.writelines(seq)
    f.close()

    f = open(filename)
    print(f.read())
    f.close()

    f = open(filename)
    print(f.read(3))
    f.close()

    f = open(filename)
    print(f.readline())
    f.close()

    f = open(filename)
    print(f.readline(2))
    f.close()

    f = open(filename)
    print(f.readlines())
    f.close()


def on_init(argument_dict):
    filename1 = "foo1.txt"
    filename2 = "foo2.txt"
    filename3 = "foo3.txt"

    second_timer(1, test_builtin_open, filename=filename1)
    second_timer(1, test_os_open, filename=filename2)
    second_timer(1, test_io_open, filename=filename3)



