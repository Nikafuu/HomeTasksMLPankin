import numpy as np
from scipy.spatial.distance import cdist



def prod_non_zero_diag(x):
    return np.prod(np.diag(x)[np.diag(x) != 0])



def are_multisets_equal(x, y):
    np.sort(x)
    np.sort(y)
    return x == y


def max_after_zero(x):
    np.max(x[1:][np.nonzero(x[:-1] == 0)])


def convert_image(img, coefs):
    return np.dot(img, coefs)


def run_length_encoding(x):
    f1 = [x[0]]
    f2 = [1]
    for i in range(1, len(x)):
        if x[i] != x[i - 1]:
            f1.append(x[i])
            f2.append(1)
        else:
            f2[-1] += 1
    return f1, f2

def pairwise_distance(x, y):
    m = [[0] * len(y) for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            m[i][j] = ((x[i][0] - y[j][0]) ** 2 + (x[i][1] - y[j][1]) ** 2) ** 0.5
    return m

def pairwise_distance_euclidean(x, y):
    return cdist(x, y, metric='euclidean')

