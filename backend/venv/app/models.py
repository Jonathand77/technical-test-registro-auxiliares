from typing import Optional
from datetime import datetime

class Actividad:
    def __init__(self, id: int, nombre_auxiliar: str, cedula: str, fecha_inicio: datetime, fecha_fin: datetime, descripcion: str, estado: str = "en espera"):
        self.id = id
        self.nombre_auxiliar = nombre_auxiliar
        self.cedula = cedula
        self.fecha_inicio = fecha_inicio
        self.fecha_fin = fecha_fin
        self.descripcion = descripcion
        self.estado = estado

db_actividades = []  # Lista para simular la base de datos