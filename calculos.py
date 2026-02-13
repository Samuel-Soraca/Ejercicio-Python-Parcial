def promedio(lista):
    return sum(lista) / len(lista)

def clasificacion_material(prom):
    if prom < 8:
        return "Bajo"
    elif prom <= 15:
        return "Estable"
    else:
        return "Alto"

def clasificacion_global(prom):
    if prom < 10:
        return "Alerta"
    elif prom < 15:
        return "Operacion normal"
    else:
        return "Jornada sobresaliente"
