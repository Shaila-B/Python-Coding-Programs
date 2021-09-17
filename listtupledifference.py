A = [1, 2, 3, (1, 2)]

print('Before Assignment : ',A[3])
print(A[3][0])
print(A[3][1])
"""
We can't change the tuple values
A[3][0]=8
print(A[3][0])
"""

A[3]=4
print('After Assignment : ',A[3])
