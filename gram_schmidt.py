"""
	Implmentation of Gram-Schmidt orthonormalization,
	also known as QR Factorization.
"""

import numpy as np

__author__ = "Phillip Wilt"
__license__ = "GPL"
__version__ = "1.0"
__email__ = "phill@phillwilt.com"

def gram_schmidt(A):
	""" Representation of Gram-Schmidt Process or QR Diagonalization 
		for an mxn system of linear equations. """
		
	m = np.shape(A)[0]
	n = np.shape(A)[1]

	Q =  np.zeros((m, m))
	R =  np.zeros((n, n)) 

	for j in xrange(n):
		
		v = A[:,j]
		
		for i in xrange(j):
			
			R[i,j] = Q[:,i].T * A[:,j]

			v = v.squeeze() - (R[i,j] * Q[:,i])

		R[j,j] =  np.linalg.norm(v)
		Q[:,j] = (v / R[j,j]).squeeze()

	return Q, R


