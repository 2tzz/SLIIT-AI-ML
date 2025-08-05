import numpy as np

a = np.array([[[1,2],[3,4],[5,6]] , 
              [[7,8],[9,10],[11,12]] , 
              [[13,14],[15,16],[17,18]]] , dtype = float)

print(a[0][2][1] )

b = np.ones([10,5] , dtype = int)

print(b)