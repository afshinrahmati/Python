import random
import my_first_module
print(my_first_module.pi)

# n
n = random.randint(5,100)
print(n)
# 0.000 ... till 4.999
m = random.random()
print(m)

heads = random.randint(0,1)
t = True
if(heads == 0):
    t = True
else:
    t = False


print(t)        
