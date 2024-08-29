import React, { useState } from 'react';
import { api } from '../services/api';

const ActividadForm = ({ onSubmit }) => {
  const [actividad, setActividad] = useState({
    nombre_auxiliar: '',
    cedula: '',
    fecha_inicio: '',
    fecha_fin: '',
    descripcion: '',
  });

  const handleChange = (e) => {
    setActividad({ ...actividad, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    await api.post('/actividades/', actividad);
    onSubmit();
  };

  return (
    <form onSubmit={handleSubmit} className="form-group">
    <input
        type="text"
        name="nombre_auxiliar"
        value={actividad.nombre_auxiliar}
        onChange={handleChange}
        className="form-control mb-2"
        placeholder="Nombre del auxiliar"
     />
    <input
        type="text"
        name="cedula"
        value={actividad.cedula}
        onChange={handleChange}
        className="form-control mb-2"
        placeholder="Cédula del auxiliar"
    />
    {/*<input
        type="text"
        name="Fecha"
        value={actividad.fecha_inicio}
        onChange={handleChange}
        className="form-control mb-2"
        placeholder="Fecha de inicio actividad"
    />
    <input
        type="text"
        name="Fecha"
        value={actividad.fecha_fin}
        onChange={handleChange}
        className="form-control mb-2"
        placeholder="Fecha de fin actividad"
    />*/}
    <input
        type="text"
        name="Descripción"
        value={actividad.descripcion}
        onChange={handleChange}
        className="form-control mb-2"
        placeholder="Descripción"
    />
    <button type="submit" className="btn btn-primary">Guardar</button>
    </form>
  );
};

export default ActividadForm;