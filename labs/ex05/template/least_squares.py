# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares solution."""
    # ***************************************************
    # INSERT YOUR CODE HERE
    # least squares: TODO
    # returns mse, and optimal weights
    N = y.shape[0]
    #w = np.dot(np.dot(np.linalg.inv(np.dot(np.transpose(tx),tx)),np.transpose(tx)),y)
    #err = y - np.dot(tx,w)
    #mse = np.dot(np.transpose(err),err)/(2*N)
    a = np.dot(np.transpose(tx),tx)
    b = np.dot(np.transpose(tx),y)
    w = np.linalg.solve(a,b)
    # ***************************************************
    
    return w
