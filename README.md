Gram-Schmidt for Python
===================

An implmentation of modified Gram-Schmidt Process for QR-Factorization in Python using numpy.

* Author: Phillip Wilt
* E-Mail: phill@phillwilt.com
* Version: 1.0
* Date: April 13th, 2013


Example 1
----------

A = np.matrix('1 0; 0 1')

Q,R = gram_schmidt.gram_schmidt(A)

print Q

[[ 1.  0.]
[ 0.  1.]] 

print R

[[ 1.  0.]
[ 0.  1.]]


Example 2
----------

A = np.matrix('1 0; 1 2')

Q,R = gram_schmidt.gram_schmidt(A)

print Q

[[ 1.  0.]
[ 0.  1.]] 

print R

[[ 1.  0.]
[ 0.  1.]]

Example 3
----------

A = np.matrix('2 3 4; 0 1 0; 0 0 1')

Q,R = gram_schmidt.gram_schmidt(A)

print Q

array([[ 1.,  0.,  0.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

print R

array([[ 2.,  3.,  4.],
       [ 0.,  1.,  0.],
       [ 0.,  0.,  1.]])

