def miss_func_num(iter):
    return [x for x in range(lst[0], lst[-1]+1)
                               if x not in iter]

# Driver code
iter = [0, 1, 2, 4, 5, 6]
miss = miss_func_num(iter)
for i in miss:
    print(i)
#print(miss)
=======
iter = [0,1,2,4,5,6,8,9]
>>>>>>> ea535d5f2d362128422ecd2c4fdbf48f6b846149
def miss_num_func():
    return [x for x in range(iter[0], iter[-1]+1)
                                if x not in iter]

print(miss_num_funct(iter))
>>>>>>> 478a3b7c3cc5c5e82136935595c679a077b1f535
