from autenticacion import login
from recolecciones import registrar_mediciones
from reporte import reporte
from registro_usuarios import registrar_usuarios

registrar_usuarios()

if login():
    registrar_mediciones()
    reporte()
else:
    print("🔒 Acceso bloqueado")