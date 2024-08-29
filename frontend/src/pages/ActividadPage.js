import React from 'react';
import { useParams } from 'react-router-dom';
import ActividadDetail from '../components/ActividadDetail';

const ActividadPage = () => {
  const { id } = useParams(); // Obtener el ID de la actividad desde la URL

  return (
    <div>
      <h1>Detalles de la Actividad</h1>
      <ActividadDetail id={id} />
    </div>
  );
};

export default ActividadPage;