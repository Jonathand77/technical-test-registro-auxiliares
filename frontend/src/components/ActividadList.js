import React, { useEffect, useState } from 'react';
import { Link } from 'react-router-dom';
import { api } from '../services/api';

const ActividadList = () => {
  const [actividades, setActividades] = useState([]);

  useEffect(() => {
    const fetchActividades = async () => {
      const response = await api.get('/actividades/');
      setActividades(response.data);
    };

    fetchActividades();
  }, []);

  return (
    <div>
      <h2>Lista de Actividades</h2>
      <ul>
        {actividades.map(actividad => (
          <li key={actividad.id}>
            <Link to={`/actividad/${actividad.id}`}>
              {actividad.descripcion}
            </Link>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default ActividadList;