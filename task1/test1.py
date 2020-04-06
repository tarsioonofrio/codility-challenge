from collections import Counter, defaultdict


def solution(T):
    n = len(T)
    c = 0
    counter = Counter(T)
    single = defaultdict(lambda: 0)
    mary = defaultdict(lambda: 0)
    rest = defaultdict(lambda: 0)
    for k, v in counter.most_common():
        if v > 1:
            for r in range(0, v - 1):
                c += 1
                mary[k] += 1
                rest[k] = mary[k] - 1
                if c == n // 2:
                    return len(mary)
        else:
            single[k] = v

    if c != n // 2:
        for k, v in single.items():
            mary[k] = 1
            c += 1
            if c == n // 2:
                break
    return len(mary)


from collections import Counter, defaultdict
def solution(T):
    n = len(T)
    c = 0
    counter = Counter(T)
    single = {}
    mary = {}
    rest = {}
    #s = [[v, k] for k, v in counter.items()]
    #s = [[v, k] for k, v in counter.items()]
    for k, v in counter.most_common():
        if v > 1:
            c += 1
            mary[k] = 1
            rest[k] = mary[k] - 1
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


T = [3, 4, 7, 7, 6, 6]

s = solution(T)
print(s)
T = [80, 80, 1000000000, 80, 80, 80, 80, 80, 80, 123456789]

s = solution(T)
print(s)
