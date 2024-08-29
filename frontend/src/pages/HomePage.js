import React from 'react';
import ActividadForm from '../components/ActividadForm';
import ActividadList from '../components/ActividadList';

const HomePage = () => {
  return (
    <div>
      <h1>Registro de Actividades</h1>
      <ActividadForm />
      <ActividadList />
    </div>
  );
};

export default HomePage;