"""
Find PI to the Nth Digit

Enter a number and have the program generate PI up to that many decimal places.
Keep a limit to how far the program will go.
"""

import math

# pi = (1 - 1/3 + 1/7 - 1/9 + 1/11 - 1/13 + 1/15) * 4

def gregory_series():
    pi = 0
    i = 1
    for j in range(10000000):
        if j % 2 != 0:
            i *= -1
        pi += 1/i
        i = abs(i) + 2

    print(pi*4)


def nilakantha_series():
    pi = 3
    i = 2
    for j in range(1000000):
        under = i * (i + 1) * (i + 2)
        if j % 2 != 0:
            under *= -1
        pi += (4 / under)
        i += 2

    print(pi)

def pi_chudnovsky(one=1000000):
    """
    Calculate pi using Chudnovsky's series

    This calculates it in fixed point, using the value for one passed in
    """
    k = 1
    a_k = one
    a_sum = one
    b_sum = 0
    C = 640320
    C3_OVER_24 = C**3 // 24
    while 1:
        a_k *= -(6*k-5)*(2*k-1)*(6*k-1)
        a_k //= k*k*k*C3_OVER_24
        a_sum += a_k
        b_sum += k * a_k
        k += 1
        if a_k == 0:
            break
    total = 13591409*a_sum + 545140134*b_sum
    pi = (426880*sqrt(10005*one, one)*one) // total
    return pi

def sqrt(n, one):
    """
    Return the square root of n as a fixed point number with the one
    passed in.  It uses a second order Newton-Raphson convergence.  This
    doubles the number of significant figures on each iteration.
    """
    # Use floating point arithmetic to make an initial guess
    floating_point_precision = 10**16
    n_float = float((n * floating_point_precision) // one) / floating_point_precision
    x = (int(floating_point_precision * math.sqrt(n_float)) * one) // floating_point_precision
    n_one = n * one
    while 1:
        x_old = x
        x = (x + n_one // x) // 2
        if x == x_old:
            break
    return x

if __name__ == "__main__":
    # nilakantha_series()

    print(pi_chudnovsky())