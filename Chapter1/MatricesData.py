from scipy import sparse
import numpy as np
# Create a 2D NumPy array with a diagonal of ones, and zeros everywhere else
eye = np.eye(20)
# Called because it sounds like the I matrix
print("NumPy array:\n{}".format(eye))

sparse_matrix = sparse.csr_matrix(eye)
#this seems to only show the non-zero entries and their locations
# It means Compressed Sparse Row (CSR) matrix, it is used to 
# have more space and compute faster
print("\nSciPy sparse CSR matrix:\n{}".format(sparse_matrix))

data = np.ones(4)
row_indices = np.arange(4)
# arrage makes list 1-4
col_indices = np.arange(4)
eye_coo = sparse.coo_matrix((data, (row_indices, col_indices)))
# represents a sparse matrix in the COOrdinate (COO) format. 
# Basically suppose we have 
# eye_coo = sparse.coo_matrix(([1, 3, 4], ([0, 2, 1], [2, 1, 0])))
# This would make the matrix
# [0, 0, 1], [4, 0, 0], [0, 3, 0]
print("COO representation:\n{}".format(eye_coo))