from __future__ import division
from collections import Counter
import math
import random

from random_variables import inverse_normal_cdf, normal_cdf

def normal_approximation_to_binomial(n, p):
    """finds mu and sigma corresponding to a Binomial(n, p)"""
    mu = p * n
    sigma = math.sqrt(n * p * (1 - p))
    return mu, sigma

# the normal cdf _is_ the probability the variable is below a threshold
def normal_probability_below(lo, mu=0, sigma=1):
    return normal_cdf(lo, mu, sigma)

# it's above the threshold if it's not below the threshold
def normal_probability_above(lo, mu=0, sigma=1):
    return 1 - normal_cdf(lo, mu, sigma)

# it's between if it's less than hi, but not less than lo
def normal_probability_between(lo, hi, mu=0, sigma=1):
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo, mu, sigma)

# it's outside if it's not between
def normal_probability_outside(lo, hi, mu=0, sigma=1):
    return 1 - normal_probability_between(lo, hi, mu, sigma)

def normal_upper_bound(probability, mu=0, sigma=1):
    """returns the z for which P(Z <= z) = probablity"""
    return inverse_normal_cdf(probability, mu, sigma)

def normal_lower_bound(probability, mu=0, sigma=1):
    """returns the z for which P(>= z) = probability"""
    return inverse_normal_cdf(1 - probability, mu, sigma)

def normal_two_sided_bounds(probability, mu=0, sigma=1):
    """returns the symmetric (about the mean) bounds 
    that contain the specified probability"""
    tail_probability = (1 - probability) / 2
    # upper bound should have tail_probility above it
    upper_bound = normal_lower_bound(tail_probability, mu, sigma)
    # lower bound should have tail_probability below it
    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

def two_sided_p_value(x, mu=0, sigma=1):
    if x >= mu:
        # if x is greather than the mean, the tail is what's greater than x
        return 2 * normal_probability_above(x, mu, sigma)
    else:
        # if x is less than the mean, the tail is wha'ts less than x
        return 2 * normal_probability_below(x, mu, sigma)

def main():
    mu_0, sigma_0 = normal_approximation_to_binomial(1000, 0.5)
    print(mu_0, sigma_0)
    print(normal_two_sided_bounds(0.95, mu_0, sigma_0))

    # 95% bounds based on assumption p is 0.5
    lo, hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

    # actual mu and sigma based on p = 0.55
    mu_1, sigma_1 = normal_approximation_to_binomial(1000, 0.55)

    # which will happen when X is still in our original interval
    type_2_probability = normal_probability_between(lo, hi, mu_1, sigma_1)
    power = 1 - type_2_probability # 0.887

    hi = normal_upper_bound(0.95, mu_0, sigma_0)
    # is 526 (< 531, since we need more probability in the upper tail)

    type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
    power = 1 - type_2_probability # 0.936

    two_sided_p_value(529.5, mu_0, sigma_0) # 0.062    


if __name__ == "__main__":
    main()
