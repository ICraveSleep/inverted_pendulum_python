import numpy as np
from numpy.linalg import inv


class Solver:

    def __init__(self, A_matrix, B_matrix, initial_conditions):
        self.A_matrix = A_matrix
        self.B_matrix = B_matrix
        self.initial_conditions = initial_conditions
        self.A_inverse = inv(A_matrix)

    def linear_slope(self,A, B, F, state, time):
        pass

