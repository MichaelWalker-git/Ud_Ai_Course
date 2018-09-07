# One of the great features of numpy is the number of built in functions
# The np.zero function allows you to fill a numpy array with 0s

# We create a 3 x 4 ndarray full of zeros.
X = np.zeros((3,4))

# We create a 3 x 2 ndarray full of ones.
X = np.ones((3,2))

# With the similar syntax, we can create a ndarray with any value
np.full(shape, constant value)

# np.eye(N) creates a square N x N ndarray
X = np.eye(5)
# [[ 1. 0. 0. 0. 0.]
#  [ 0. 1. 0. 0. 0.]
#  [ 0. 0. 1. 0. 0.]
#  [ 0. 0. 0. 1. 0.]
#  [ 0. 0. 0. 0. 1.]]

# Create ndarrays that have evenly spaced values

x = np.arange(10)
# x = [0 1 2 3 4 5 6 7 8 9]

x = np.arange(4,10)
# x = [4 5 6 7 8 9]

# non-integer steps are required, it is usually better to use the function np.linspace()
# np.linspace(start, stop, N) function returns N evenly spaced numbers over the closed interval [start, stop]
x = np.linspace(0,25,10)
# x = [ 0. 2.77777778 5.55555556 8.33333333 11.11111111 13.88888889 16.66666667 19.44444444 22.22222222 25. ]

# with 50 excluded. We then reshape it to a 5 x 2 ndarray
X = np.linspace(0,50,10, endpoint=False).reshape(5,2)
# X =
#  [[ 0. 5.]
#  [ 10. 15.]
#  [ 20. 25.]
#  [ 30. 35.]
#  [ 40. 45.]]

# np.random.normal(mean, standard deviation, size=shape)

####################
# Delete items in nparray
# np.delete(ndarray, elements, axis)
# axis = 0 is used to select rows, and axis = 1 is used to select columns
# np.insert(ndarray, index, elements, axis)

# np.vstack() function for vertical stacking, or the np.hstack() function for horizontal stacking
Y = np.array([[3,4],[5,6]])
w = np.hstack((Y,([1],[2])))

# w =
# [[3 4 1]
#  [5 6 2]]


###################
# Slice ndarrays
# 1. ndarray[start:end]
# 2. ndarray[start:]
# 3. ndarray[:end]

# We select all the elements in the 3rd column
X = np.X(20).reshape(4, 5)

# X =
# [[ 0 1 2 3 4]
#  [ 5 6 7 8 9]
#  [10 11 12 13 14]
#  [15 16 17 18 19]]


q = X[:,2]
# q = [ 2 7 12 17]


# We select all the elements that are in the 1st through 3rd rows and in the 3rd to 4th columns
Y = X[:3,2:5]

# Y =
# [[ 2 3 4]
#  [ 7 8 9]
#  [12 13 14]]


# We select all the elements in the 3rd column but return a rank 2 ndarray
R = X[:,2:3]
# R =
# [[ 2]
#  [ 7]
#  [12]
#  [17]]

# Important: when we perform slices on ndarrays and save them into new variables, as we did above, the data is not copied into the new variable.
# We select all the elements that are in the 2nd through 4th rows and in the 3rd to 4th columns
Z = X[1:4,2:5]
Z[2,2] = 555

# Z =
# [[ 7 8 9]
#  [12 13 14]
#  [17 18 19]]

###############################3
# NumPy also offers built-in functions to select specific elements within ndarrays.
# For example, the np.diag(ndarray, k=N) function extracts the elements along the diagonal defined by N.

# We use Boolean indexing to select elements in X:
print('The elements in X that are greater than 10:', X[X > 10])
print('The elements in X that less than or equal to 7:', X[X <= 7])
print('The elements in X that are between 10 and 17:', X[(X > 10) & (X < 17)])

# We create a rank 1 ndarray
x = np.array([1,2,3,4,5])

# We create a rank 1 ndarray
y = np.array([6,7,2,8,4])

print('The elements that are both in x and y:', np.intersect1d(x,y))
print('The elements that are in x that are not in y:', np.setdiff1d(x,y))
print('All the elements of x and y:',np.union1d(x,y))

###################### Sorting ####################
# np.sort() is used as a function, it sorts the ndrrays out of place (not directly mutate)
# However, when you use  ndarray.sort(), it sorts the ndarray in place (mutate)

# np.unique(x)

# When sorting rank 2 ndarrays, we need to specify to the np.sort() function
# whether we are sorting by rows or columns. This is done by using the axis keyword.

# Original X =
# [[6 1 7 6 3]
#   [3 9 8 3 5]
#   [6 5 8 9 3]
#   [2 1 5 7 7]
#   [9 8 1 9 8]]

np.sort(X, axis=0)

# X with sorted columns :
# [[2 1 1 3 3]
#   [3 1 5 6 3]
#   [6 5 7 7 5]
#   [6 8 8 9 7]
#   [9 9 8 9 8]]

# We sort the rows of X and print the sorted array
print()
print('X with sorted rows :\n', np.sort(X, axis = 1))

# X with sorted rows :
# [[1 3 6 6 7]
#   [3 3 5 8 9]
#   [3 5 6 8 9]
#   [1 2 5 7 7]
#   [1 8 8 9 9]]

###################### Quiz ##############

import numpy as np

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
# Afterwards use Boolean indexing to pick out only the odd numbers in the array

# Create a 5 x 5 ndarray with consecutive integers from 1 to 25 (inclusive).
X = np.arange(1,26).reshape(5,5)

# Use Boolean indexing to pick out only the odd numbers in the array
Y = X[X % 2 == 1]
# print(X)

###################### Broadcasting ##############

# Broadcasting is the term used to describe how NumPy handles element-wise arithmetic operations with ndarrays of different shapes
# broadcasting is used implicitly when doing arithmetic operations between scalars and ndarrays.

x = np.array([1,2,3,4])
y = np.array([5.5,6.5,7.5,8.5])

print('add(x,y) = ', np.add(x,y))
# add(x,y) = [ 6.5 8.5 10.5 12.5]

print('subtract(x,y) = ', np.subtract(x,y))
# subtract(x,y) = [-4.5 -4.5 -4.5 -4.5]

print('multiply(x,y) = ', np.multiply(x,y))
# multiply(x,y) = [ 5.5 13. 22.5 34. ]

print('divide(x,y) = ', np.divide(x,y))
# divide(x,y) = [ 0.18181818 0.30769231 0.4 0.47058824]

print('EXP(x) =', np.exp(x))
# EXP(x) = [ 2.71828183 7.3890561 20.08553692 54.59815003]

print('SQRT(x) =',np.sqrt(x))
# SQRT(x) = [ 1. 1.41421356 1.73205081 2. ]

print('POW(x,2) =',np.power(x,2)) # We raise all elements to the power of 2
# POW(x,2) = [ 1 4 9 16]

X = np.array([[1,2], [3,4]])

print('Average of all elements in X:', X.mean())
print('Average of all elements in the columns of X:', X.mean(axis=0))
print('Average of all elements in the rows of X:', X.mean(axis=1))

print('Sum of all elements in X:', X.sum())
print('Sum of all elements in the columns of X:', X.sum(axis=0))
print('Sum of all elements in the rows of X:', X.sum(axis=1))

print('Standard Deviation of all elements in X:', X.std())
print('Standard Deviation of all elements in the columns of X:', X.std(axis=0))
print('Standard Deviation of all elements in the rows of X:', X.std(axis=1))

print('Median of all elements in X:', np.median(X))
print('Median of all elements in the columns of X:', np.median(X,axis=0))
print('Median of all elements in the rows of X:', np.median(X,axis=1))

print('Maximum value of all elements in X:', X.max())
print('Maximum value of all elements in the columns of X:', X.max(axis=0))
print('Maximum value of all elements in the rows of X:', X.max(axis=1))

print('Minimum value of all elements in X:', X.min())
print('Minimum value of all elements in the columns of X:', X.min(axis=0))
print('Minimum value of all elements in the rows of X:', X.min(axis=1))

###################### Quiz ##############


# Use Broadcasting to create a 4 x 4 ndarray that has its first
# column full of 1s, its second column full of 2s, its third
# column full of 3s, etc..
a = np.ones((4,4))
b = np.array([1,2,3,4])

X = np.multiply(a,b)

X = np.ones((4,4)) * np.arange(1,5)

# LAB

Mean normalization will scale the data instead of makeing the alue be between 0 and 1


