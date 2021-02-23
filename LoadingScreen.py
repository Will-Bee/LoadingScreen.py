from time import sleep
from os import system
from colorama import Fore as f

x = 0 

for i in range(100):
    x +=1
    y = 100 - x
    print(x, "/ 100%")
    print("|", x * "=", "|", y * "-", "|")
    sleep(0.01)
    system('cls')





### importy, os.system pro cls command, time.sleep pro timeout v loadingu, bude nahrazeno v implementaci do kodu ###

### x = 0                                                  |načtení hodnoty "x" jako nula, x je počet procent pro template
### for i in range(100):                                   |navyšuje hodnotu "i" s každým cyklem, pokud je hodnota pod 100 tak se cyklus opakuje
###     x +=1                                              |navyšuje hodnotu "x" neboli procenta
###     y = 100 - x                                        |určuje hodnotu "y" jako počet co zbývá do sta procent
###     print(x, "/ 100%")                                 |vypíše "x" / 100, např.: 50 / 100%, závisí na hodnotě "x"
###     print("|", x * "=", "|", y * "-", "|")             |vypíše graf následovně: "x" krát rovnáse, |, "y" krát pomlčka
###     sleep(0.01)                                        |timeout v loadingu, bude nahrazeno v implementaci do kodu
###     system('cls')                                      |vymaže celý příkazový řádek
