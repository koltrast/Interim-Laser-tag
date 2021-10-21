#coding:utf8

# importing the modules
import random

# dictionnary
orig_list = [
    "A01", "A02", "A03", "A04", "B01", "B02", "B03", "B04", "C01", "C02", "C03", "C04", "D01", "D02", "D03", "D04", "E01", "E02", "E03", "E04", "F01", "F02", "F03", "F04", "G01", "G02", "G03", "G04", "I01", "I02", "I03", "I04", "J01", "J02", "J03", "J04", "K01", "K02", "K03", "K04", "L01", "L02", "L03", "L04", "M01", "M02", "M03", "M04", "N01", "N02", "N03", "N04", "O01", "O02", "O03", "O04", "P01", "P02", "P03", "P04", "Q01", "Q02", "Q03", "Q04", "R01", "R02", "R03", "R04", "S01", "S02", "S03", "S04", "T01", "T02", "T03", "T04", "U01", "U02", "U03", "U04", "V01", "V02", "V03", "V04", "W01", "W02", "W03", "W04", "X01", "X02"]


# variable


# function
def sample_key():
    n = random.randint(12,16)
    global sample_list
    sample_list = random.choices(orig_list, k=n)
    print(f"There is {n} items to prepare. Here they are : \n")
    print(*sample_list, sep = "\n")


# exec
sample_key()

