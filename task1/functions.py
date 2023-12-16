def prod_non_zero_diag(x):
    pr = 1
    for i in range(len(x)):
        if i == len(x[i]):
            return pr
        if x[i][i] != 0:
            pr *= x[i][i]
    return pr
        


def are_multisets_equal(x, y):
    x.sort()
    y.sort()
    return x == y


def max_after_zero(x):
    maxi = 0
    for i in range(1, len(x)):
        if x[i - 1] == 0 and maxi < x[i]:
            maxi = x[i]


def convert_image(img, coefs):
    ot = []
    for i in range(len(img)):
        ot.append([])
        for j in range(len(img[i])):
            ot[-1].append(img[i][j][0] * coefs[0] +
                     img[i][j][1] * coefs[1] +
                     img[i][j][2] * coefs[2])
    return ot

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
    ot = [[0] * len(y) for _ in range(len(x))]
    for i in range(len(x)):
        for j in range(len(y)):
            ot[i][j] = ((x[i][0] - y[j][0]) ** 2 + (x[i][1] - y[j][1]) ** 2) ** 0.5
    return ot

