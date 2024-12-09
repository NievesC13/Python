import os as o 
import msvcrt as m

o.system("cls")

x = 0
i = 0

password = input("Ingresa un Password: ")

while x == 0:
    if m():
        password = password + m.getch()
        print("*")
        i += 1 
    if password  == "cf1":
        print("Encontraste la clave")
        x = 1
    if i == 3 :
        print("Fallaste, vuele a intenarlo")
        o.system("cls")
