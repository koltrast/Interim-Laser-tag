#!/usr/bin/env python

# modules
import os
import random
import time
from time import sleep
import pygame

# global variables
logo = ('''
UNION PRAGMATIQUE                  #PLAYTIME 
▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄
███ ██ ██ ▄▄ ████ ██ ██ ▄▄ ████ ██ ██ ▄▄ ███
███ ██ ██ ▀▀ ████ ██ ██ ▀▀ ████ ██ ██ ▀▀ ███
███▄▀▀▄██ ███████▄▀▀▄██ ███████▄▀▀▄██ ██████
▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀
INTERIM LASER TAG                       2024
   ''')
n = random.randint(5,8)
a = 1
b = 1
p = 0

# functions

def generate_list(prefix, start_letter, end_letter, start_number, end_number):
    import string
    # Get the list of letters from start_letter to end_letter
    letters = string.ascii_uppercase[string.ascii_uppercase.index(start_letter):string.ascii_uppercase.index(end_letter) + 1]
    # Generate the list based on the given ranges
    result_list = [f"{prefix}{letter}0{num}" for letter in letters for num in range(start_number, end_number + 1)]
    return result_list

def sample_key():
    global sample_list
    sample_list = random.choices(orig_list, k=n)
    print(f"There are {n} items to prepare. Here they are :\n")
    print(*sample_list, sep = "\n")

def sample_list_to_txt():
    with open("sample_list.tmp", "w", encoding="utf-8") as f:
        f.write(f"{logo}\n\nPour commencer, scannez le code barre START\n\nIl y a {n} objets à préparer.\nLes voici :\n\n")
        for items in sample_list:
            f.writelines(items+ "\n")
        f.write("\n\nQuand vous aurez fini,\nscannez le code barre STOP\n\n\n--------------------------------------------")

def sample_list_to_printer():
    os.system("lpr -P EPSON_TM-T20III sample_list.tmp -o cpi=16 -o lpi=7")
    os.remove("sample_list.tmp")

def penalities():
    pygame.mixer.music.load('sound/wrong.wav')
    pygame.mixer.music.play()
    global p
    p = p + 10
    print(p, " seconds of penalities !")

def ragequitter():
    import os
    with open("ragequit.tmp", "w", encoding="utf-8") as f:
        f.write("Vous êtes VIRÉ !\nVous n’avez pas terminé votre commande.\n\n\n--------------------------------------------")
    os.system("lpr -3 EPSON_TM-T20III ragequit.tmp -o cpi=16 -o lpi=7")
    os.remove("ragequit.tmp")

def score_to_txt():
    with open("score.tmp", "w", encoding="utf-8") as f:
        f.write(f"{logo}\n\n")
        f.write(f"Vous avez préparé une commande de {n} objets \n en {total:.5g} secondes\n\n")
        if p == 0:
            f.write(f"\n\n--------------------------------------------")
        elif p > 0:
            f.write(f"cependant vous avez fait\n{int(p/10)} erreurs, totalisant\n{p} secondes\n\n")
            f.write(f"Votre temps retenu est de\n{totalp:.5g} secondes\n\n\n--------------------------------------------")
        else:
            print("no penalities")
        f.write("\nVotre nom : ____________________________\n\nImprimé en 2 exemplaires\n\n--------------------------------------------")

def score_to_printer():
    os.system("lpr -P EPSON_TM-T20III score.tmp -o cpi=16 -o lpi=7")
    os.system("lpr -P EPSON_TM-T20III score.tmp -o cpi=16 -o lpi=7")
    os.remove("score.tmp")

# exec

orig_list = generate_list("UP-K21-", 'A', 'R', 1, 6)
pygame.mixer.init()
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
            pygame.mixer.music.load('sound/start.wav')
            pygame.mixer.music.play()
            while pygame.mixer.music.get_busy():
                pygame.time.Clock().tick(10)
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
            if i == n and a == 0:
                pygame.mixer.music.load('sound/complete.wav')
                pygame.mixer.music.play()
            else:
                print("No sound for quitters")
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
                    b = b - 1
                    a = 1
                    sleep(15)
                    n = random.randint(5,8)
                else:
                    b = 1
        else:
            b = 1
