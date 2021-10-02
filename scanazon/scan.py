# ----- PROCESS -----
# read the dictionnary and create an random list
# print the random list
# wait for start then launch timer
# scan process + wait for end signal
# stop the timer
# add penalties
# print results then start back

# ===================


# importing the modules
import time
import random

# definition
x = random.randint(12,16)
def list_barcode():
    original_list = (open("list.txt","r").readlines())
    sample_list = random.choices(original_list, k=x)
    print(f"There is {x} barcodes to scan. Here they are : \n")
    print(*sample_list, sep = "\n")

a = 1
 
# exec
list_barcode()
while a == 1:
    print("Scan the start barcode")
    if input() == 0:
        t0 = time.time()
        i = 0 
        while i < x:
            print(str(x - i) + " to scan")
            scn = input()
            print("barcode is : ", scn)
            i = i + 1
        while a == 1:
            print("Scan the end barcode")
            if input() == 9:
                t1 = time.time()
                total = t1-t0
                print("Your time is ", total)
                a = a - 1
            else:
                print("Nope")
                a = 1
    else:
        print("Nope")
        a = 1
