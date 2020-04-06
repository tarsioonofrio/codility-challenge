import random


def solution(indices, k=2):
    seed = 42
    sn = round(len(indices) / k)
    random.Random(seed).shuffle(indices)
    subsets = [indices[x:x + sn] for x in range(0, len(indices), sn)]
    kfolds = [0] * k * 2
    for r in range(k):
        train = subsets[0:r] + subsets[r+1:]
        if type(train[0]) == list:
            train = [v for sublist in train for v in sublist]
        valid = subsets[r]
        if type(valid[0]) == list:
            valid = [v for sublist in valid for v in sublist]
        kfolds[r*2] = train
        kfolds[r*2 + 1] = valid

    return kfolds


indices = [1, 2, 3]
k = 2
#indices = list(range(10))
s = solution(indices, k=2)
print(s)


I = [[3], [2, 1], [2, 1], [3]]