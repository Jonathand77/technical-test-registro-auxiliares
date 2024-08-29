from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class ActividadBase(BaseModel):
    nombre_auxiliar: str
    cedula: str
    fecha_inicio: datetime
    fecha_fin: datetime
    descripcion: str

class ActividadCreate(ActividadBase):
    pass

class Actividad(ActividadBase):
    id: int
    estado: str

    class Config:
        orm_mode = True