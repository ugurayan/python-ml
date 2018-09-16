########################################################
# Ugur Ayan
# ugur.ayan@ugurayan.com.tr
# www.ugurayan.com.tr
# August 25, 2018
########################################################

import math


def add_vector(v1, v2):
    """adds two vectors"""
    return [w1 + w2 for w1, w2 in zip(v1, v2)]


def subtract_vector(v1, v2):
    """subtracts two vectors"""
    return [w1 - w2 for w1, w2 in zip(v1, v2)]


def sum_vector(vectors):
    """sums all vectors"""
    return reduce(add_vector, vectors)


def sum_of_squares(v):
    """v_1*v_1 + ... + v_n*v_n"""
    return dot_product(v, v)


def multiply_scalar(c, v):
    """c is a number, v is a vector"""
    return [c * v_i for v_i in v]


def mean_vector(vectors):
    """compute the vector whose ith element is the mean of the ith elements of the input vectors"""
    n = len(vectors)
    return multiply_scalar(1 / n, sum_vector(vectors))


def dot_product(v1, v2):
    """v1_1*v2_1 + ... + v1_n*v2_n"""
    return sum(v1_i * v2_i for v1_i, v2_i in zip(v1, v2))


# "range" already means something in Python, so we'll use a different name
def data_range(x):
    return max(x) - min(x)


def de_mean(x):
    """translate x by subtracting its mean (so the result has mean 0)"""
    x_bar = mean(x)
    return [x_i - x_bar for x_i in x]


def standard_deviation(x):
    return math.sqrt(variance(x))


def variance(x):
    """assumes x has at least two elements"""
    n = len(x)
    deviations = de_mean(x)
    return sum_of_squares(deviations) / (n - 1)


def norm(v1, v2, l):
    if l == 1:
        """if l=1, L1 Norm or Manhattan distance, city block distance, snake distance """
        return sum(abs(v1_i - v2_i) for v1_i, v2_i in zip(v1, v2))
    elif l == 2:
        """if l=2, L2 Norm or Euclidean distance"""
        return math.sqrt(sum((v1_i - v2_i) ** 2 for v1_i, v2_i in zip(v1, v2)))
    else:
        """if l=p, Lp Norm"""
        return math.pow(sum((v1_i - v2_i) ** 2 for v1_i, v2_i in zip(v1, v2)), l)


def euclidean_distance(v1, v2):
    return norm(v1, v2, 2)


def manhatten_distance(v1, v2):
    return norm(v1, v2, 1)


def get_row(A, i):
    return A[i]  # A[i] is already the ith row


def get_column(A, j):
    return [A_i[j]  # jth element of row A_i
            for A_i in A]  # for each row A_i


def make_matrix(num_rows, num_cols, entry_fn):
    """returns a num_rows x num_cols matrix whose (i,j)th entry is entry_fn(i, j)"""
    return [[entry_fn(i, j)  # given i, create a list
             for j in range(num_cols)]  # [entry_fn(i,0),...]
            for i in range(num_rows)]  # create one list for each i


def is_diagonal(i, j):
    """1's on the 'diagonal',0's everywhere else"""
    return 1 if i == j else 0


def mean(x):
    return sum(x) / len(x)


def median(v):
    """finds the 'middle-most' value of v"""
    n = len(v)
    sorted_v = sorted(v)
    midpoint = n // 2
    if n % 2 == 1:
        # if odd, return the middle value
        return sorted_v[midpoint]
    else:
        # if even, return the average of the middle values
        lo = midpoint - 1
        hi = midpoint
        return (sorted_v[lo] + sorted_v[hi]) / 2


def correlation(x, y):
    stdev_x = standard_deviation(x)
    stdev_y = standard_deviation(y)
    if stdev_x > 0 and stdev_y > 0:
        return covariance(x, y) / stdev_x / stdev_y
    else:
        return 0  # if no variation, correlation is zero


def covariance(x, y):
    n = len(x)
    return dot_product(de_mean(x), de_mean(y)) / (n - 1)


def uniform_pdf(x):
    return 1 if x >= 0 and x < 1 else 0


def uniform_cdf(x):
    "returns the probability that a uniform random variable is <= x"
    if x < 0:
        return 0  # uniform random is never less than 0
    elif x < 1:
        return x  # e.g. P(X <= 0.4) = 0.4
    else:
        return 1  # uniform random is always less than 1


def normal_pdf(x, mu=0, sigma=1):
    sqrt_two_pi = math.sqrt(2 * math.pi)
    return (math.exp(-(x - mu) ** 2 / 2 / sigma ** 2) / (sqrt_two_pi * sigma))


def normal_cdf(x, mu=0, sigma=1):
    return (1 + math.erf((x - mu) / math.sqrt(2) / sigma)) / 2


def inverse_normal_cdf(p, mu=0, sigma=1, tolerance=0.00001):
    """find approximate inverse using binary search"""
    # if not standard, compute standard and rescale
    if mu != 0 or sigma != 1:
        return mu + sigma * inverse_normal_cdf(p, tolerance=tolerance)
    low_z, low_p = -10.0, 0  # normal_cdf(-10) is (very close to) 0
    hi_z, hi_p = 10.0, 1  # normal_cdf(10)  is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z + hi_z) / 2  # consider the midpoint
        mid_p = normal_cdf(mid_z)  # and the cdf's value there
        if mid_p < p:
            # midpoint is still too low, search above it
            low_z, low_p = mid_z, mid_p
        elif mid_p > p:
            # midpoint is still too high, search below it
            hi_z, hi_p = mid_z, mid_p
        else:
            break
    return mid_z


def bernoulli_trial(p):
    return 1 if random.random() < p else 0


def binomial(n, p):
    return sum(bernoulli_trial(p) for _ in range(n))