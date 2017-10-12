# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # ridge regression: TODO
    M = tx.shape[1]
    I = np.identity(M)
    a = np.dot(np.transpose(tx),tx) + 2*len(y)*lambda_*I
    b = np.dot(np.transpose(tx),y)
    w = np.linalg.solve(a,b)
    # ***************************************************
    #raise NotImplementedError
    return w
