import React from 'react';
import { Link } from 'react-router-dom';
import './Navbar.css';
import logo from '../assets/img/LisLogo.png';


const Navbar = () => {
  return (
    <nav className="navbar">
      <img src={logo} alt="Logo" />
      <ul>
        <li><Link to="/">Inicio</Link></li>
        <li><Link to="/actividad">Lista de Actividades</Link></li>
        <li><Link to="/actividad/nueva">Nueva Actividad</Link></li>
        <li><Link to="/actividad/:id">Detalles de Actividades</Link></li>
        <li><Link to="/actividad/editar/:id">Editar Actividades</Link></li>
      </ul>
    </nav>
  );
};

export default Navbar;