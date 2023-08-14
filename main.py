#!/usr/bin/python3
from art import *
from termcolor import colored
import os

print(colored(text2art ("VlainScanner", font="random")))
print(colored('Created by Vlain LOM\n\n'.center(60)))

def main() :
    print("1- Scanned a target\n2- Scanned multiple targets")

    sc = True
    while sc :

        Choixnbr = input("? ")

        if Choixnbr == "1" :
            import onecible.portscan

        elif Choixnbr == "2" :
            import multicibles.portscantargets

        elif Choixnbr == "exit" :
            sc = False
        elif Choixnbr == "clear" :
            os.system("clear")

        else:
            print("\nChoisir un nombre entre 1-2")

if __name__ == "__main__":
    main()
