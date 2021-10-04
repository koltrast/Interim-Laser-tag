import random
randomlist = []
for i in range(50): 
    n = random.randint(3560238704691,4033657720409)
    randomlist.append(n)
randomlist.sort()
print(*randomlist, sep = "\n")
f=open("serials.txt","w")
f.write(f"{randomlist}")
 
