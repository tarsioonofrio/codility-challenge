from collections import Counter
from itertools import takewhile
import random
import time

debug = False


def solution_codility(T):
    n = len(T)
    c = 0
    counter = Counter(T)
    single = {}
    mary = {}
    for k, v in counter.most_common():
        if v > 1:
            c += 1
            mary[k] = 1
        else:
            single[k] = v
        if c == n // 2:
            break

    for k, v in single.items():
        mary[k] = 1
        c += 1
        if c == n // 2:
            break
    return len(mary)



def solution_fast(T):
    """
    This solution does not guarantee the correct separation of the sweets,
    half for mary and half for her brother,
    but it does guarantee that mary will receive the correct number of types of sweets

    *********
    I just found out that this implementation is a fraction of a second faster than the other sauhsahusahusahu
    too much work for nothing
    *********

    :param T:
    :return:
    """
    half = len(T)//2
    d = Counter(T)

    # unecessary but work, i dont need of keys and values
    # g = ({k: v} for k, v in d.most_common())
    # f = lambda x: x[list(x.keys())[0]] > 1
    # s = list(takewhile(f, g))

    # i will use a generator inside a takewhile with a lambda function
    # i think this will be more fast but in fact im not sure if this will be faster
    g = (v for k, v in d.most_common())
    f = lambda x: x > 1
    s = [abs(1 - x) for x in list(takewhile(f, g))]
    counter = sum(s)
    length = len(s)

    for k, v in d.most_common()[length:]:
        print(k, v)
        counter += 1
        if counter == half:
            break
    return counter


def solution_correct(T):
    """
    this solution guarantees that the correct separation of the sweets will occur

    :param T:
    :return:
    """
    counter = 0
    half = len(T)//2
    # split candies in different bowls
    d = Counter(T)
    # TODO replace mary_bag with d, remove mary_bag too
    for k, v in list(d.most_common()):
        # if i have more than one candie
        if v > 1:
            if half - counter >= v:
                counter = counter + v - 1
                d[k] = 1
            else:
                counter = half
                d[k] = abs(v - half)
        else:
            del d[k]
            counter += 1

        if counter == half:
            break

    if debug:
        print(d)

    return len(d)


def main():
    print("Test with solution_correct function")
    print("Correctness test")
    T0 = [3, 4, 7, 7, 6, 6]
    s = solution_correct(T0)
    print("Solution is {} for {}".format(s, T0))

    T1 = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]
    s = solution_correct(T1)
    print("Solution is {} for {}".format(s, T1))

    for r in range(10):
        t = [random.randrange(2, 10, 2) for _ in range(random.randrange(2, 10, 2))]
        s = solution_correct(t)
        print("Solution is {} for {}".format(s, t))

    print("Performance test")
    n = int(10)
    start = time.time()
    for r in range(n):
        t = [random.randrange(2, int(1e9), 2) for _ in range(int(1e5))]
        s = solution_correct(t)

    end = time.time()
    total = end - start
    print("Total time of {} executions: {}, Mean {}".format(n, total, total/n))

    print("**************")

    print("Test with solution_fast function")
    print("Correctness test")
    s = solution_fast(T0)
    print("Solution is {} for {}".format(s, T0))
    s = solution_fast(T1)
    print("Solution is {} for {}".format(s, T1))

    for r in range(10):
        t = [random.randrange(2, 10, 2) for _ in range(random.randrange(2, 10, 2))]
        s = solution_correct(t)
        print("Solution is {} for {}".format(s, t))

    print("Performance test")
    n = int(10)
    start = time.time()
    for r in range(n):
        t = [random.randrange(2, int(1e9), 2) for _ in range(int(1e5))]
        s = solution_correct(t)

    end = time.time()
    total = end - start
    print("Total time of {} executions: {}, Mean {}".format(n, total, total/n))


if __name__ == "__main__":
    main()








