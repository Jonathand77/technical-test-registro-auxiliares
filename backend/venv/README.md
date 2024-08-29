# technical-test-2024-2

## **Project Description:**

En el laboratorio contamos con varios proyectos desarrollados en tecnologías de backend que dan soporte a las diferentes actividades que se realizan al interior del mismo, es por esto que es importante para un auxiliar de programación tener conocimientos básicos para dar soporte y/o agregar nuevas funcionalidades a dichos proyectos.
Uno de los deberes de los auxiliares de programación y administrativos es el registro de horas
trabajadas. Teniendo en cuenta lo anterior, se desarrolló un proyecto backend (REST API) para REGISTRO DE ACTIVIDADES REALIZADAS con los
siguientes requerimientos:

## **Technologies Used:** 

- **Programming languages:** Python<img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/python/python-original.svg" alt="python" width="40" height="40"/> GIT<img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> Swagger.

## Getting Started 🚀

# Proyecto de Registro de Actividades

## Requisitos

- Python 3.8 o superior
- Swagger

## Instalación

Sigue estos pasos para configurar y ejecutar el proyecto en tu entorno local.

### 1. Clonar el Repositorio

Primero, clona el repositorio desde GitHub:

```
git clone https://github.com/tuUsuario/technical-test-2024-2.git
cd technical-test-2024-2
```


### Crear un Entorno Virtual 📋

_Crea y activa un entorno virtual para el proyecto:_


```
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```


### Instalar Dependencias 🔧

_Instala las dependencias necesarias usando pip:_


```
pip install -r requirements.txt
```


_Ejecución del Servidor_
_Para iniciar el servidor de la API, ejecuta el siguiente comando:_


```
uvicorn app.main:app --reload
```

_El servidor estará disponible en http://127.0.0.1:8000._

## Uso de la API 🚀

- La API proporciona varias rutas para interactuar con las actividades. Puedes acceder a la documentación interactiva de la API en http://127.0.0.1:8000/docs.

## Endpoints

POST /actividades/

Crea una nueva actividad.

Request Body:


```
{
  "nombre_auxiliar": "Nombre del Auxiliar",
  "cedula": "12345678",
  "fecha_inicio": "2024-08-24T08:00:00",
  "fecha_fin": "2024-08-24T17:00:00",
  "descripcion": "Descripción de la actividad"
}
```


Response:


```
{
  "nombre_auxiliar": "Nombre del Auxiliar",
  "cedula": "12345678",
  "fecha_inicio": "2024-08-24T08:00:00",
  "fecha_fin": "2024-08-24T17:00:00",
  "descripcion": "Descripción de la actividad"
}
```


GET /actividades/

Obtiene todas las actividades o filtra por estado.

Query Parameters:

estado (opcional): Filtra actividades por estado (en espera, aprobado, rechazado).
Response:


```
[
  {
    "id": 1,
    "nombre_auxiliar": "Nombre del Auxiliar",
    "cedula": "12345678",
    "fecha_inicio": "2024-08-24T08:00:00",
    "fecha_fin": "2024-08-24T17:00:00",
    "descripcion": "Descripción de la actividad",
    "estado": "en espera"
  }
]
```


GET /actividades/{id}

Obtiene una actividad específica por su ID.

Response:


```
{
  "id": 1,
  "nombre_auxiliar": "Nombre del Auxiliar",
  "cedula": "12345678",
  "fecha_inicio": "2024-08-24T08:00:00",
  "fecha_fin": "2024-08-24T17:00:00",
  "descripcion": "Descripción de la actividad",
  "estado": "en espera"
}
```


PATCH /actividades/{id}/estado

Actualiza el estado de una actividad.

Request Body:


```
{
  "estado": "aprobado"  // O "rechazado"
}
```


Response:


```
{
  "id": 1,
  "nombre_auxiliar": "Nombre del Auxiliar",
  "cedula": "12345678",
  "fecha_inicio": "2024-08-24T08:00:00",
  "fecha_fin": "2024-08-24T17:00:00",
  "descripcion": "Descripción de la actividad",
  "estado": "aprobado"
}
```


PATCH /actividades/{id}

Actualiza los campos de una actividad específica por ID.

Request Body:


```
{
  "nombre_auxiliar": "Nuevo Nombre",
  "fecha_fin": "2024-08-24T18:00:00"
}
```


Response:


```
{
  "id": 1,
  "nombre_auxiliar": "Nuevo Nombre",
  "cedula": "12345678",
  "fecha_inicio": "2024-08-24T08:00:00",
  "fecha_fin": "2024-08-24T18:00:00",
  "descripcion": "Descripción de la actividad",
  "estado": "en espera"
}
```


GET /actividades/horas

Muestra las horas trabajadas en un margen de tiempo específico por un auxiliar.

Query Parameters:

cedula: Cédula del auxiliar.
fecha_inicio: Fecha de inicio del rango (ISO 8601).
fecha_fin: Fecha de fin del rango (ISO 8601).
Response:


```
{
  "cedula": "12345678",
  "total_horas": 8
}
```


GET /actividades/estado

Muestra todas las actividades según su estado (en espera, aprobado, rechazado).

Query Parameters:

estado: Estado de las actividades a filtrar.
Response:


```
[
  {
    "id": 1,
    "nombre_auxiliar": "Nombre del Auxiliar",
    "cedula": "12345678",
    "fecha_inicio": "2024-08-24T08:00:00",
    "fecha_fin": "2024-08-24T17:00:00",
    "descripcion": "Descripción de la actividad",
    "estado": "en espera"
  }
]
```


GET /actividades/cantidad

Calcula la cantidad de actividades realizadas por un auxiliar específico.

Query Parameters:

cedula: Cédula del auxiliar.
Response:


```
{
  "cedula": "12345678",
  "cantidad": 5
}
```


## Authors ✒️

* **Jonathan Fernandez** - [Jonathand77](https://github.com/Jonathand77)


## Expressions of Gratitude 🎁

* Tell others about this project 📢
* Say thank you publicly 🤓.

--- 
⌨️ by [Jonathand77](https://github.com/Jonathand77) 😊