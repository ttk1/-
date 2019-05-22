#!/bin/python3
# coding:utf-8


def hanoi_f(n, a, b, c):
    if n == 1:
        print('%s -> %s' % (a, c))
    else:
        hanoi_f(n-1, a, c, b)
        hanoi_f(1, a, b, c)
        hanoi_f(n-1, b, a, c)


def hanoi(n):
    hanoi_f(n, 'a', 'b', 'c')


if __name__ == '__main__':
    hanoi(5)
