import json

def cargar_usuarios():
    with open("usuarios.json", "r", encoding="utf-8") as archivo:
        return json.load(archivo)

def login():
    usuarios = cargar_usuarios()
    intentos = 3

    while intentos > 0:
        correo = input("Correo: ")
        password = input("Password: ")

        for u in usuarios:
            if u["correo"] == correo and u["password"] == password:
                print("\n///// Inicio de sesión exitoso /////")
                print("👤 Nombre:", u["nombre"])
                print("🏢 Empresa:", u["empresa"])
                print("💼 Cargo:", u["rol"])
                return True

        intentos -= 1
        print("❌ Datos incorrectos. Intentos restantes:", intentos)

    return False
