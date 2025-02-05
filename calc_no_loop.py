# coding: utf-8
import numpy as np
def calc_no_loop(new_points, points):
    m = len(new_points)
    n = len(points)
    a = new_points[:,np.newaxis,:]
    b = points[np.newaxis,:,:]
    difference = a - b
    square = difference ** 2
    return np.sum(square, axis=2)
