#!/usr/bin/env python

# list
orig_list = ["UP-K21-A00", "UP-K21-A01", "UP-K21-A02", "UP-K21-A03", "UP-K21-A04", "UP-K21-A05", "UP-K21-A06", "UP-K21-A07", "UP-K21-A08", "UP-K21-A09", "UP-K21-B00", "UP-K21-B01", "UP-K21-B02", "UP-K21-B03", "UP-K21-B04", "UP-K21-B05", "UP-K21-B06", "UP-K21-B07", "UP-K21-B08", "UP-K21-B09", "UP-K21-C00", "UP-K21-C01", "UP-K21-C02", "UP-K21-C03", "UP-K21-C04", "UP-K21-C05", "UP-K21-C06", "UP-K21-C07", "UP-K21-C08", "UP-K21-C09", "UP-K21-D00", "UP-K21-D01", "UP-K21-D02", "UP-K21-D03", "UP-K21-D04", "UP-K21-D05", "UP-K21-D06", "UP-K21-D07", "UP-K21-D08", "UP-K21-D09", "UP-K21-E00", "UP-K21-E01", "UP-K21-E02", "UP-K21-E03", "UP-K21-E04", "UP-K21-E05", "UP-K21-E06", "UP-K21-E07", "UP-K21-E08", "UP-K21-E09", "UP-K21-F00", "UP-K21-F01", "UP-K21-F02", "UP-K21-F03", "UP-K21-F04", "UP-K21-F05", "UP-K21-F06", "UP-K21-F07", "UP-K21-F08", "UP-K21-F09", "UP-K21-G00", "UP-K21-G01", "UP-K21-G02", "UP-K21-G03", "UP-K21-G04", "UP-K21-G05", "UP-K21-G06", "UP-K21-G07", "UP-K21-G08", "UP-K21-G09", "UP-K21-H00", "UP-K21-H01", "UP-K21-H02", "UP-K21-H03", "UP-K21-H04", "UP-K21-H05", "UP-K21-H06", "UP-K21-H07", "UP-K21-H08", "UP-K21-H09", "UP-K21-I00", "UP-K21-I01", "UP-K21-I02", "UP-K21-I03", "UP-K21-I04", "UP-K21-I05", "UP-K21-I06", "UP-K21-I07", "UP-K21-I08", "UP-K21-I09", "UP-K21-J00", "UP-K21-J01", "UP-K21-J02", "UP-K21-J03", "UP-K21-J04", "UP-K21-J05", "UP-K21-J06", "UP-K21-J07", "UP-K21-J08", "UP-K21-J09", "UP-K21-K00", "UP-K21-K01", "UP-K21-K02", "UP-K21-K03", "UP-K21-K04", "UP-K21-K05", "UP-K21-K06", "UP-K21-K07", "UP-K21-K08", "UP-K21-K09", "UP-K21-L00", "UP-K21-L01", "UP-K21-L02", "UP-K21-L03", "UP-K21-L04", "UP-K21-L05", "UP-K21-L06", "UP-K21-L07", "UP-K21-L08", "UP-K21-L09", "UP-K21-M00", "UP-K21-M01", "UP-K21-M02", "UP-K21-M03", "UP-K21-M04", "UP-K21-M05", "UP-K21-M06", "UP-K21-M07", "UP-K21-M08", "UP-K21-M09", "UP-K21-N00", "UP-K21-N01", "UP-K21-N02", "UP-K21-N03", "UP-K21-N04", "UP-K21-N05", "UP-K21-N06", "UP-K21-N07", "UP-K21-N08", "UP-K21-N09", "UP-K21-O00", "UP-K21-O01", "UP-K21-O02", "UP-K21-O03", "UP-K21-O04", "UP-K21-O05", "UP-K21-O06", "UP-K21-O07", "UP-K21-O08", "UP-K21-O09", "UP-K21-P00", "UP-K21-P01", "UP-K21-P02", "UP-K21-P03", "UP-K21-P04", "UP-K21-P05", "UP-K21-P06", "UP-K21-P07", "UP-K21-P08", "UP-K21-P09", "UP-K21-Q00", "UP-K21-Q01", "UP-K21-Q02", "UP-K21-Q03", "UP-K21-Q04", "UP-K21-Q05", "UP-K21-Q06", "UP-K21-Q07", "UP-K21-Q08", "UP-K21-Q09", "UP-K21-R00", "UP-K21-R01", "UP-K21-R02", "UP-K21-R03", "UP-K21-R04", "UP-K21-R05", "UP-K21-R06", "UP-K21-R07", "UP-K21-R08", "UP-K21-R09", "UP-K21-S00", "UP-K21-S01", "UP-K21-S02", "UP-K21-S03", "UP-K21-S04", "UP-K21-S05", "UP-K21-S06", "UP-K21-S07", "UP-K21-S08", "UP-K21-S09", "UP-K21-T00", "UP-K21-T01", "UP-K21-T02", "UP-K21-T03", "UP-K21-T04", "UP-K21-T05", "UP-K21-T06", "UP-K21-T07", "UP-K21-T08", "UP-K21-T09", "UP-K21-U00", "UP-K21-U01", "UP-K21-U02", "UP-K21-U03", "UP-K21-U04", "UP-K21-U05", "UP-K21-U06", "UP-K21-U07", "UP-K21-U08", "UP-K21-U09", "UP-K21-V00", "UP-K21-V01", "UP-K21-V02", "UP-K21-V03", "UP-K21-V04", "UP-K21-V05", "UP-K21-V06", "UP-K21-V07", "UP-K21-V08", "UP-K21-V09", "UP-K21-W00", "UP-K21-W01", "UP-K21-W02", "UP-K21-W03", "UP-K21-W04", "UP-K21-W05", "UP-K21-W06", "UP-K21-W07", "UP-K21-W08", "UP-K21-W09", "UP-K21-X00", "UP-K21-X01", "UP-K21-X02", "UP-K21-X03", "UP-K21-X04", "UP-K21-X05", "UP-K21-X06", "UP-K21-X07", "UP-K21-X08", "UP-K21-X09", "UP-K21-Y00", "UP-K21-Y01", "UP-K21-Y02", "UP-K21-Y03", "UP-K21-Y04", "UP-K21-Y05", "UP-K21-Y06", "UP-K21-Y07", "UP-K21-Y08", "UP-K21-Y09", "UP-K21-Z00", "UP-K21-Z01", "UP-K21-Z02", "UP-K21-Z03", "UP-K21-Z04", "UP-K21-Z05", "UP-K21-Z06", "UP-K21-Z07", "UP-K21-Z08", "UP-K21-Z09"]

# importing the modules
import random
import time
from time import sleep
from playsound import playsound

# global variables
logo = ('''
 __   __  _______ 
|  | |  ||       |
|  | |  ||    _  |
|  |_|  ||   |_| |
|       ||    ___|
|       ||   |    
|_______||___| 2021
INTERIM-LASER-TAG
   ''')
n = random.randint(5,8)
a = 1
b = 1
p = 0

# functions
def sample_key():
    global sample_list
    sample_list = random.choices(orig_list, k=n)
    print(f"There are {n} items to prepare. Here they are :\n")
    print(*sample_list, sep = "\n")

def sample_list_to_txt():
    with open("sample_list.tmp", "w", encoding="utf-8") as f:
        f.write(f"{logo}\n\nPour commencer scannez le\ncode barre \"START\"\n\nIl y a {n} objets à préparer.\nLes voici :\n\n")
        for items in sample_list:
            f.writelines(items+ "\n")
        f.write("\n\nQuand vous aurez fini,\nn’oubliez pas de scanner\nle code barre \"STOP\"\n\n\n----------------------------")

def sample_list_to_printer():
    import os
    os.system("lpr -P EPSON_TM-T20III sample_list.tmp")

def penalities():
    playsound('sound/wrong.wav')
    global p
    p = p + 10
    print(p, " seconds of penalities !")

def ragequitter():
    import os
    with open("ragequit.tmp", "w", encoding="utf-8") as f:
        f.write("Vous êtes VIRÉ !\nVous n’avez pas terminé\nvotre commande.\n\n\n----------------------------")
    os.system("lpr -3 EPSON_TM-T20III ragequit.tmp")

def score_to_txt():
    with open("score.tmp", "w", encoding="utf-8") as f:
        f.write(f"{logo}\n\n")
        f.write(f"Vous avez préparé votre\ncommande de {n} objets en\n{total:.5g} secondes\n")
        if p == 0:
            f.write(f"\n\n\n----------------------------")
        elif p > 0:
            f.write(f"cependant vous avez fait\n{int(p/10)} erreurs, totalisant\n{p} secondes\n\n")
            f.write(f"Votre temps retenu est de\n{totalp:.5g} secondes\n\n\n----------------------------")
        else:
            print("no penalities")
        f.write("Votre nom : _______________\n\nImprimé en 2 exemplaires\n\n----------------------------")

def score_to_printer():
    import os
    os.system("lpr -P EPSON_TM-T20III score.tmp")

# exec
while a == 1:
    a = 0
    b = 1
    p = 0
    sample_key()
    sample_list_to_txt()
    sample_list_to_printer()
    while b == 1:
        print("Scan the start barcode")
        if input() == "START":
            playsound('sound/start.wav')
            t0 = time.time()
            i = 0
            while i < n and a == 0:
                print(str(n - i) + " to scan")
                scan = input()
                if scan in sample_list:
                    print(scan, "is in the list")
                    sample_list.remove(scan)
                    i = i + 1
                elif scan == "STOP":
                    print("You’re fired")
                    ragequitter()
                    b = 0
                    a = 1
                    sleep(15)
                else:
                    penalities()
                    print("You dumb idiot")
            playsound('sound/complete.wav')
            while b == 1:
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
                    score_to_printer()
                    b = b - 1
                    a = 1
                    sleep(15)
                    n = random.randint(5,8)
                else:
                    b = 1
        else:
            b = 1
