from app.models import Actividad, db_actividades
from app.schemas import ActividadCreate
from typing import List, Optional
from datetime import datetime

def create_actividad(actividad: ActividadCreate) -> Actividad:
    new_id = len(db_actividades) + 1
    new_actividad = Actividad(id=new_id, **actividad.dict())
    db_actividades.append(new_actividad)
    return new_actividad

def get_actividades(estado: str = None) -> List[Actividad]:
    if estado:
        return [actividad for actividad in db_actividades if actividad.estado == estado]
    return db_actividades

def get_actividad_by_id(id: int) -> Optional[Actividad]:
    for actividad in db_actividades:
        if actividad.id == id:
            return actividad
    return None

def update_actividad(actividad_id: int, actividad: ActividadCreate) -> Optional[Actividad]:
    for act in db_actividades:
        if act.id == actividad_id:
            act.nombre_auxiliar = actividad.nombre_auxiliar
            act.cedula = actividad.cedula
            act.fecha_inicio = actividad.fecha_inicio
            act.fecha_fin = actividad.fecha_fin
            act.descripcion = actividad.descripcion
            return act
    return None

def update_estado_actividad(actividad_id: int, estado: str) -> Optional[Actividad]:
    for act in db_actividades:
        if act.id == actividad_id:
            act.estado = estado
            return act
    return None

def get_actividades_by_fecha(fecha: str) -> List[Actividad]:
    fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
    return [act for act in db_actividades if act.fecha_inicio.date() == fecha_dt.date()]

def get_horas_trabajadas(cedula: str, fecha_inicio: str, fecha_fin: str) -> int:
    fecha_inicio_dt = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fecha_fin_dt = datetime.strptime(fecha_fin, "%Y-%m-%d")
    total_horas = 0
    for act in db_actividades:
        if act.cedula == cedula and fecha_inicio_dt <= act.fecha_inicio <= fecha_fin_dt:
            horas = (act.fecha_fin - act.fecha_inicio).total_seconds() / 3600
            total_horas += horas
    return int(total_horas)

def get_actividades_by_cedula(cedula: str) -> List[Actividad]:
    return [actividad for actividad in db_actividades if actividad.cedula == cedula]

def count_actividades_by_fecha(fecha: datetime) -> int:
    return len(get_actividades_by_fecha(fecha))

def get_cantidad_actividades_por_auxiliar(cedula: str) -> int:
    return len(get_actividades_by_cedula(cedula))

def count_actividades_by_cedula(cedula: str) -> int:
    return len(get_actividades_by_cedula(cedula))

def get_cantidad_actividades_por_fecha(fecha: str) -> int:
    fecha_dt = datetime.strptime(fecha, "%Y-%m-%d")
    return len([act for act in db_actividades if act.fecha_inicio.date() == fecha_dt.date()])

def calculate_horas_trabajadas(cedula: str, start_time: datetime, end_time: datetime) -> float:
    actividades = [actividad for actividad in db_actividades if actividad.cedula == cedula and actividad.fecha_inicio >= start_time and actividad.fecha_fin <= end_time]
    total_hours = sum((actividad.fecha_fin - actividad.fecha_inicio).total_seconds() for actividad in actividades) / 3600.0
    return total_hours

def get_actividades_by_estado(estado: str) -> List[Actividad]:
    return [act for act in db_actividades if act.estado == estado]