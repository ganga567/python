import numpy as np
givenArray = np.ones((2,2,3),dtype=int)
print(" The Like array is : In", givenArray)
likeArray = np.zeros_like(givenArray)
print("The Zeros like array is :In ", likeArray)
print("The shape of like array is : ", likeArray.shape)