# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

from collections import deque, OrderedDict
import math
import random
import time

debug = False


def solution_codility(N):
    s = deque()
    for p in range(30):
        for q in range(30):
            n = (2 ** p) * (3 ** q)
            s.append(n)
    s = list(s)
    s.sort()

    return s[N]


def solution(N):
    d = OrderedDict()
    d[1] = None
    i2 = 1
    i3 = 1
    while True:
        # test two multiples
        v2 = i2 * 2
        l2 = math.log(v2, 2)
        # test if module for 3 is zero
        q3, r3 = divmod(v2, 3)
        if r3 == 0:
            d[v2] = None
            # i2 += 1
            i3 = q3 + 1
            if debug:
                print("{} % 3 == 0".format(v2))
        # test if is power of two
        if l2.is_integer():
            d[v2] = None
            if debug:
                print("{} is power of two".format(v2))
            # i2 += 1
        i2 += 1

        # test three multiples
        v3 = i3 * 3
        l3 = math.log(v3, 3)
        # test if module for 2 is zero
        q2, r2 = divmod(v3, 2)
        if r2 == 0:
            d[v3] = None
            # i3 += 1
            i2 = q2 + 1
            if debug:
                print("{} % 2 == 0".format(v3))
        # test if is power of two
        if l3.is_integer():
            d[v3] = None
            if debug:
                print("{} is power of three".format(v3))
            # i3 += 1
        i3 += 1
        if debug:
            print("length of d: {}".format(len(d)))

        if len(d) >= N + 1:
            break

    return list(d.keys())[N]


def main():
    A = [0] * 10
    A[0] = 1
    A[1] = 2
    A[2] = 3
    A[3] = 4
    A[4] = 6
    A[5] = 8
    A[6] = 9
    A[7] = 12
    A[8] = 16
    A[9] = 18

    print("Correctness test")
    for n in A:
        s = solution(n)
        print("Solution for N = {} is {}".format(n, s))

    for r in range(10):
        n = random.randint(0, 200)
        s = solution(n)
        print("Solution for N = {} is {}".format(n, s))

    print("Performance test")
    n = int(10e3)
    start = time.time()
    for r in range(n):
        n = random.randint(0, 200)
        s = solution(n)

    end = time.time()
    total = end - start
    print("Total time of {} executions: {}, Mean {}".format(n, total, total/n))


if __name__ == "__main__":
    main()



