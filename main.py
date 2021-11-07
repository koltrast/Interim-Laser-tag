#!/usr/bin/env python

orig_list = ["A01", "A02", "A03", "A04", "B01", "B02", "B03", "B04", "C01", "C02", "C03", "C04", "D01", "D02", "D03", "D04", "E01", "E02", "E03", "E04", "F01", "F02", "F03", "F04", "G01", "G02", "G03", "G04", "I01", "I02", "I03", "I04", "J01", "J02", "J03", "J04", "K01", "K02", "K03", "K04", "L01", "L02", "L03", "L04", "M01", "M02", "M03", "M04", "N01", "N02", "N03", "N04", "O01", "O02", "O03", "O04", "P01", "P02", "P03", "P04", "Q01", "Q02", "Q03", "Q04", "R01", "R02", "R03", "R04", "S01", "S02", "S03", "S04", "T01", "T02", "T03", "T04", "U01", "U02", "U03", "U04", "V01", "V02", "V03", "V04", "W01", "W02", "W03", "W04", "X01", "X02"]


# importing the modules
import random
import time
import decimal

# global variables
n = random.randint(2,3)
a = 1
p = 0

# functions
def sample_key():
    global sample_list
    sample_list = random.choices(orig_list, k=n)
    print(f"There are {n} items to prepare. Here they are : \n")
    print(*sample_list, sep = "\n")
    
def sample_list_to_txt():
    with open("sample_list.tmp", "w", encoding="utf-8") as f:
        f.write(f"Il y a {n} objets à préparer. Les voici :\n\n")
        for items in sample_list:
            f.writelines(items+ "\n")
        f.write("\nScannez le code barre \"START\" \n\n Quand vous aurez fini, n’oubliez pas de scanner le code barre \"STOP\"")

def sample_list_to_printer():
    import os
    os.system("lpr -P EPSON_TM-T20III sample_list.tmp")

def penalities():
    global p
    p = p + 10
    print(p, " seconds of penalities !")

def score_to_txt():
    with open("score.tmp", "w", encoding="utf-8") as g:
        g.write(f"Vous avez préparé votre commande en {total} secondes\n\n")
        if p > 0 :
            g.write(f"cependant vous avez fait {int(p/10)} erreurs, totalisant {p} secondes\n\n")
            g.write(f"Votre temps retenu est de {totalp} secondes")
        else:
            print("no penalities")


def score_to_printer():
    import os
    os.system("lpr -P EPSON_TM-T20III score.tmp")

# exec
sample_key()
sample_list_to_txt()
sample_list_to_printer()
while a == 1:
    print("Scan the start barcode")
    if input() == "START":
        t0 = time.time()
        i = 0
        while i < n :
            print(str(n - i) + " to scan")
            scan = input()
            if scan in sample_list:
                print(scan, "is in the list")
                sample_list.remove(scan)
                i = i + 1
            elif scan == "STOP":
                print("This can’t stop")
            else:
                penalities()
                print("You dumb idiot")
        while a == 1:
            print("Scan the stop bar code")
            if input() == "STOP":
                t1 = time.time()
                total = t1-t0
                totalp = total + p
                print("Your time is ", total)
                print("Your penalties are ", p)
                print("Your final time is", totalp)
                score_to_txt()
                score_to_printer()
                a = a - 1
            else:
                a = 1
    else:
        a = 1
