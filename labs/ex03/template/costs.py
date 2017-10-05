# -*- coding: utf-8 -*-
"""Function used to compute the loss."""

import numpy as np

def compute_loss(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    N = y.shape[0]
    dyf = y - tx.dot(w)
    mse = np.sum(dyf*dyf)/(2*N)
    
    #raise NotImplementedError
    return mse

def compute_mse(y, tx, w):
    """Calculate the loss.

    You can calculate the loss using mse or mae.
    """
    N = y.shape[0]
    dyf = y - tx.dot(w)
    mse = np.sum(dyf*dyf)/(2*N)
    
    #raise NotImplementedError
    return mse