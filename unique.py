import numpy as np
myarray = np.array([[1,3,4,5],[7,3,4,2],[3,2,6,8]])
unique_value,counts=np.unique(myarray,return_counts=True)
unique_value_list=unique_value[counts==1]
print(unique_value_list)