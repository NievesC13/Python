import os as o
import random 
import time
import msvcrt 
o.system("cls")

def contar_consonantes(palabra):
    consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    conteo = sum(1 for letra in palabra if letra in consonantes)
    return conteo

def generar_numeros_aleatorios():
    for _ in range(10):
        numero_aleatorio = round(random.uniform(3.1, 4.7), 2)
        print(numero_aleatorio)
        time.sleep(0.5)

def generate_randon_numbers():
    for _ in range(5) :
        random_number = round(random.uniform(981, 984.5))
        print(random_number)
        time.sleep(0.5)

def main():
    # Paso 1: Pedir al usuario que ingrese una frase de cuatro palabras
    frase = input("Ingresa una frase de cuatro palabras: ")
    palabras = frase.split()

    if len(palabras) != 4:
        print("Error: La frase debe contener exactamente cuatro palabras.")
        return

    # Paso 2: Verificar si la segunda palabra contiene una cantidad par de consonantes
    segunda_palabra = palabras[1]
    cantidad_consonantes = contar_consonantes(segunda_palabra)

    if cantidad_consonantes % 2 == 0:
        print("La segunda palabra tiene una cantidad par de consonantes.")

        # Paso 3: Esperar a que el usuario ingrese la letra "a"
        while True:
            if msvcrt.kbhit():
                tecla = msvcrt.getch().decode().lower()
                if tecla == 'a' or tecla == 'A':
                    print("Se ingresó la letra 'a/A'. Generando números aleatorios...")
                    generar_numeros_aleatorios()
                else :
                    tecla = msvcrt.getch().decode().lower()
                    if tecla == 'f' or tecla == 'F':
                        print("Se ingresó la letra 'f/F'.")
                        print(f"La Segunda Palabra es \"{segunda_palabra}\" y la cantidad de consonantes son \"{cantidad_consonantes}\"")
                        break
    else:
        print("La segunda palabra no tiene una cantidad par de consonantes.")
        generate_randon_numbers()

    # Paso 4: Generar 10 números aleatorios entre 3.1 y 4.7 en intervalos de 0.5 segundos
    
if __name__ == "__main__":
    main()
