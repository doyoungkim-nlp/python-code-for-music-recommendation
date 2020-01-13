#!/usr/bin/env python
# coding: utf-8

# In[14]:


import random
import numpy as np
mat=[]
f = open("songList.txt", 'r')
while True:
    line = f.readline()[:-1]
    if not line: break
    print(line)
    mat.append(line)
f.close()
random.shuffle(mat)#None
np.savetxt('random_test.txt',mat, fmt='%s')


# In[ ]:




