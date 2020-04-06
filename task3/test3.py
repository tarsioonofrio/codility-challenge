import random


def solution_codility(indices, k=2):
    """
    I think i lost the solution i send to codility but they are simply and have one error
    I need to unpack the train list

    :param indices:
    :param k:
    :return:
    """


def solution_correct(indices, k=2):
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



def main():
    indices = [1, 2, 3]
    k = 2
    s = solution(indices, k)
    print("For indices {} with k {}, these are the kfolds: {}".format(indices, k, s))


if __name__ == "__main__":
    main()

