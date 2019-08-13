import math;
def corr(a, b):
    sum_ab = 0
    sum_a = 0
    sum_b = 0
    sum_a_sqr = 0
    sum_b_sqr = 0
    n = min([len(a), len(b)]);
    for i in range(0, n):
        sum_ab += a[i] * b[i]
        sum_a += a[i]
        sum_b += b[i]
        sum_a_sqr += pow(a[i], 2)
        sum_b_sqr += pow(b[i], 2)
    return (sum_ab/n - sum_a/n * sum_b/n) / (math.sqrt(sum_a_sqr/n - pow(sum_a/n, 2)) * math.sqrt(sum_b_sqr/n - pow(sum_b/n, 2)))
