import numpy as np
array = np.array([1,2,3,'one','two','three'])
print array
print 'size:',array.ndim
print 'shape:',array.shape
array2 = array.reshape(2,3)
