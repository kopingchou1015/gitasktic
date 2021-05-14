<<<<<<< HEAD
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  3 13:59:42 2021

@author: new
"""

def miss_num_func(iter):
    return [x for x in range(iter[0], iter[-1]+1) 
                               if x not in iter]

iter= [0,1,2,4,5,6,8,9]

miss= miss_num_func(iter)
print(miss) 

=======
"""
This file is part of the github course W2 task
"""
import numpy as np

iter = [0, 1, 2, 4, 5, 6]
def miss_num_func(iter):
    '''
    This function takes in a list called "iter" with items in serial order,
    and returns the missing item.
    1. Make another list called "compare" with the biggest item in iter list as the final item
    2. Compare "compare" with "iter", and returns the missing item
    '''
    n = iter[-1]
    compare = np.arange(0, n+1, 1).tolist()
    same_index = []
    for i in range(len(iter)):
        for j in range(len(compare)):
            if iter[i] == compare[j]:
                same_index.append(j)
    all_index = list(range(0, n+1))
    lis_dif = [i for i in all_index if i not in same_index]

    item = []
    for i in range(len(lis_dif)):
        item.append(compare[lis_dif[i]])

    return item

miss = miss_num_func(iter)

miss
>>>>>>> 854256ecb160a53b69c28fd44ff42f35c21e8ed1
