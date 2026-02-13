recolecciones = {
    "PET": [],
    "CARTON": [],
    "VIDRIO": [],
    "METAL": []
}

def registrar_mediciones():
    for material in recolecciones:
        print("\nRegistro para:", material)

        for i in range(20):
            while True:
                dato = input(f"Ingrese kg medición {i+1}: ")

                if dato.strip() == "":
                    print("😞 No puede estar vacío")
                    continue

                try:
                    kg = float(dato)

                    if kg < 0:
                        print("😞 No se permiten números negativos")
                        continue

                    recolecciones[material].append(kg)
                    break

                except ValueError:
                    print("😞 Ingrese solo números válidos")
