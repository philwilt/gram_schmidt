Gram-Schmidt for Python
===================

An implmentation of modified Gram-Schmidt Process for QR-Factorization in Python using numpy.

* Author: Phillip Wilt
* E-Mail: phill@phillwilt.com
* Version: 1.0
* Date: April 13th, 2013


Example 1
----------
```python
>>> A = np.matrix('1 0; 0 1')

>>> Q,R = gram_schmidt.gram_schmidt(A)

>>> print Q

[[ 1.  0.]
[ 0.  1.]] 

>>> print R

[[ 1.  0.]
[ 0.  1.]]

```

Example 2
----------
```python
>>> A = np.matrix('1 0; 1 2')

>>> Q,R = gram_schmidt.gram_schmidt(A)

>>> print Q

[[ 1.  0.]
[ 0.  1.]] 

>>> print R

[[ 1.  0.]
[ 0.  1.]]

```

Example 3
----------
```python
>>> A = np.matrix('2 3 4; 1 3 0; 0 0 1')
>>> Q,R = gram_schmidt.gram_schmidt(A)
>>> Q
array([[  8.94427191e-01,  -4.47213595e-01,   1.33226763e-15],
       [  4.47213595e-01,   8.94427191e-01,  -6.66133815e-16],
       [  0.00000000e+00,   0.00000000e+00,   1.00000000e+00]])
>>> R
array([[ 2.23606798,  4.02492236,  3.57770876],
       [ 0.        ,  1.34164079, -1.78885438],
       [ 0.        ,  0.        ,  1.        ]])
```

