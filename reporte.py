from calculos import promedio, clasificacion_material, clasificacion_global
from recolecciones import recolecciones

def reporte():
    promedios = []

    print("\n===== REPORTE FINAL =====")

    for material in recolecciones:
        prom = promedio(recolecciones[material])
        promedios.append(prom)

        print(material,
              "- Promedio:", round(prom,2),
              "- Clasificacion:", clasificacion_material(prom))

    prom_global = sum(promedios)/len(promedios)

    print("\nPromedio Global:", round(prom_global,2))
    print("Estado Global:", clasificacion_global(prom_global))
