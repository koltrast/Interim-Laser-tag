import random
randomlist = []
for i in range(100): 
    n = random.randint(3560238704691,4033657720409)
    randomlist.append(n)
print(randomlist)
f=open("serials.txt","w")
f.write(f"{randomlist}")
 
