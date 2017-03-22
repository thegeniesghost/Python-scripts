from sys import exit
import random
a = input("How many?\n> ")
s = input("Enter range start: ")
e = input("Enter range end: ")
def printer(s, e):
    print random.choice(range(s, e))
def printerx(a):
    for i in range(a):
        printer(s, e)

printerx(a)