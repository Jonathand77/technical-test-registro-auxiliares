import React, { useEffect, useState } from 'react';
import { api } from '../services/api';

const ActividadDetail = ({ id }) => {
  const [actividad, setActividad] = useState(null);

  useEffect(() => {
    const fetchActividad = async () => {
      const response = await api.get(`/actividades/${id}`);
      setActividad(response.data);
    };

    fetchActividad();
  }, [id]);

  if (!actividad) return <div>Cargando...</div>;

  return (
    <div>
      <h2>Detalles de Actividad</h2>
      <p>Nombre: {actividad.nombre_auxiliar}</p>
      <p>Descripción: {actividad.descripcion}</p>
      {/* Otros detalles */}
    </div>
  );
};

export default ActividadDetail;