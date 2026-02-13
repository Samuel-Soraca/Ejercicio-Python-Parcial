import json
import os

def cargar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r", encoding="utf-8") as archivo:
            return json.load(archivo)
    return []

def guardar_usuarios(lista):
    with open("usuarios.json", "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo, indent=4, ensure_ascii=False)

def registrar_usuarios():

    opcion = input("¿Desea registrar usuarios? (s/n): ").lower()

    if opcion != "s":
        print("\n📁 No se registraron usuarios")
        return

    usuarios = cargar_usuarios()

    while True:

        print("\n===== REGISTRO DE 5 USUARIOS =====")

        for i in range(5):

            print(f"\nUsuario #{i+1}")

            nombre = input("Nombre: ")
            correo = input("Correo: ")
            password = input("Contraseña: ")
            empresa = input("Empresa: ")
            rol = input("Rol: ")

            usuario = {
                "nombre": nombre,
                "correo": correo,
                "password": password,
                "empresa": empresa,
                "rol": rol
            }

            usuarios.append(usuario)

        guardar_usuarios(usuarios)

        print("\n✅ Usuarios guardados correctamente")

        continuar = input("\n¿Desea registrar otros 5 usuarios? (s/n): ").lower()

        if continuar != "s":
            print("\n📁 Registro finalizado")
            break
