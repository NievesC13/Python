#login

import getpass

# Usuarios registrados
users = {
    "juan": "1234",
    "maria": "abcd",
    "pedro": "qwerty"
}

# Función para validar el usuario y contraseña ingresados
def login():
    username = input("Ingrese su nombre de usuario: ")
    password = getpass.getpass("Ingrese su contraseña: ")
    if username in users and users[username] == password:
        print("Inicio de sesión exitoso")
    else:
        print("Usuario o contraseña incorrectos")

# Ejecutar función de inicio de sesión
login()