from fastapi import FastAPI, HTTPException
from typing import List
from app import models, schemas, crud

app = FastAPI()

@app.post("/actividades/", response_model=schemas.Actividad)
def create_actividad(actividad: schemas.ActividadCreate):
    return crud.create_actividad(actividad)

@app.get("/actividades/", response_model=List[schemas.Actividad])
def read_actividades(estado: str = None):
    return crud.get_actividades(estado)

@app.get("/actividades/cedula/{cedula}", response_model=List[schemas.Actividad])
def get_actividades_by_cedula(cedula: str):
    actividades = crud.get_actividades_by_cedula(cedula)
    return actividades

@app.get("/actividades/auxiliar/{cedula}/cantidad", response_model=int)
def get_cantidad_actividades_por_auxiliar(cedula: str):
    cantidad = crud.get_cantidad_actividades_por_auxiliar(cedula)
    return cantidad

# Actualizar los Campos de una Actividad Específica por ID
@app.patch("/actividades/{actividad_id}", response_model=schemas.Actividad)
def update_actividad(actividad_id: int, actividad: schemas.ActividadCreate):
    updated_actividad = crud.update_actividad(actividad_id, actividad)
    if updated_actividad is None:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    return updated_actividad

# Marcar una Actividad como Aprobada o Rechazada
@app.patch("/actividades/{actividad_id}/estado", response_model=schemas.Actividad)
def update_estado_actividad(actividad_id: int, estado: str):
    if estado not in ["aprobado", "rechazado", "en espera"]:
        raise HTTPException(status_code=400, detail="Estado inválido")
    
    updated_actividad = crud.update_estado_actividad(actividad_id, estado)
    if updated_actividad is None:
        raise HTTPException(status_code=404, detail="Actividad no encontrada")
    return updated_actividad

# Obtener Actividades por Fecha Específica
@app.get("/actividades/fecha/{fecha}", response_model=List[schemas.Actividad])
def get_actividades_by_fecha(fecha: str):
    actividades = crud.get_actividades_by_fecha(fecha)
    return actividades

# Mostrar Horas Trabajadas en un Margen de Tiempo Específico
@app.get("/actividades/horas", response_model=int)
def get_horas_trabajadas(cedula: str, fecha_inicio: str, fecha_fin: str):
    horas_trabajadas = crud.get_horas_trabajadas(cedula, fecha_inicio, fecha_fin)
    return horas_trabajadas

# Calcular la Cantidad de Actividades Hechas en un Día Específico
@app.get("/actividades/cantidad/{fecha}", response_model=int)
def get_cantidad_actividades_por_fecha(fecha: str):
    cantidad = crud.get_cantidad_actividades_por_fecha(fecha)
    return cantidad

# 6. Mostrar Todas las Actividades Aprobadas, Rechazadas o en Espera
@app.get("/actividades/estado/{estado}", response_model=List[schemas.Actividad])
def get_actividades_by_estado(estado: str):
    if estado not in ["aprobado", "rechazado", "en espera"]:
        raise HTTPException(status_code=400, detail="Estado inválido")
    
    actividades = crud.get_actividades_by_estado(estado)
    return actividades

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)