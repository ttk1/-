#!/bin/python3
# coding:utf-8

from benchmarker import Benchmarker
import numpy as np


def mp(p1, p2):
    if np.array_equal(p1, [-1, 0]) and np.array_equal(p2, [1, 0]):
        return np.array([0, 1])
    p = (p1 + p2) / 2
    return p / np.sqrt(np.sum(p**2))


def f(x):
    if x < 0 or 1 < x:
        raise Exception('xは0以上1以下の範囲で指定してください.')
    t1 = 1
    t2 = 0
    p1 = np.array([-1, 0])
    p2 = np.array([1, 0])
    while np.abs(t1 - t2) > 0.00001:
        m = (t1 + t2) / 2
        if m > x:
            t1 = m
            p1 = mp(p1, p2)
        else:
            t2 = m
            p2 = mp(p1, p2)
    return p1


def sin(x):
    return f(x/np.pi)[1]


def cos(x):
    return f(x/np.pi)[0]


def tan(x):
    p = f(x/np.pi)
    return p[1] / p[0]


if __name__ == '__main__':
    with Benchmarker(1000, width=20) as bench:
        @bench('hoge')
        def _(bm):
            for _ in bm:
                sin(0.33)

        @bench('piyo')
        def _(bm):
            for _ in bm:
                np.sin(0.33)
