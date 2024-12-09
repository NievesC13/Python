def encontrar_elemento_pico(nums):
    # Buscamos un elemento pico
    for i in range(2, len(nums) - 1):
        if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
            return i

    # Si no encontramos un pico, devolvemos None
    return None

def main():
    try:
        # Ingresar la lista de números por consola
        entrada = input("Ingresa una lista de números separados por espacios: ")
        lista = [int(x) for x in entrada.split()]

        # Encontrar el elemento pico
        indice_pico = encontrar_elemento_pico(lista)
        if indice_pico is not None:
            print(f"Índice del elemento pico: {indice_pico}")
        else:
            print("No se encontró ningún elemento pico en la lista.")
    except ValueError:
        print("Error: La lista debe contener números enteros.")

if __name__ == "__main__":
    main()
