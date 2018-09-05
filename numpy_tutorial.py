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
Delete items in nparray
# np.delete(ndarray, elements, axis)
# axis = 0 is used to select rows, and axis = 1 is used to select columns
# np.insert(ndarray, index, elements, axis)

# np.vstack() function for vertical stacking, or the np.hstack() function for horizontal stacking
Y = np.array([[3,4],[5,6]])
w = np.hstack((Y,([1],[2])))

# w =
# [[3 4 1]
#  [5 6 2]]