import numpy as np
import scipy.signal as spy

def conv2d(X, W, p=(0,0), s=(1,1)):
	W_rot = np.array(W)[::-1, ::-1]
	X_orig = np.array(X)
	n1 = X_orig.shape[0] + 2*p[0]
	n2 = X_orig.shape[1] + 2*p[1]
	X_padded = np.zeros(shape=(n1,n2))
	X_padded[p[0]:p[0] + X_orig.shape[0], p[1]: p[1] + X_orig.shape[1]] = X_orig
	res = []
		
	for i in range (0, int ((X_padded.shape[0] - W_rot.shape[0])/s[0]) + 1, s[0]):
		res.append([])
		for j in range(0, int ((X_padded.shape[1] - W_rot.shape[1])/s[1]) + 1, s[1]):
			X_sub = X_padded[i:i+W_rot.shape[0], j:j+W_rot.shape[1]]
			res[-1].append(np.sum(X_sub * W_rot))
	return (np.array(res))

# Testing:
X = [[1, 3, 2, 4], [5, 6, 1, 3], [1, 2, 0, 2] , [3, 4, 3, 2]]
W = [[1, 0, 3], [1, 2, 1], [0, 1, 1]]

print
print('Convolution 2D Implementation:')
print(conv2d(X, W, p=(1,1), s=(1,1)))

print
print('SciPy Results:')
print(spy.convolve2d(X, W, mode='same'))
