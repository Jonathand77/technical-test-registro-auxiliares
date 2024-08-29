import './styles.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import HomePage from './pages/HomePage';
import ActividadPage from './pages/ActividadPage';
import ActividadList from './components/ActividadList';
import ActividadForm from './components/ActividadForm';
import ActividadDetail from './components/ActividadDetail';
import Navbar from './components/Navbar';
import { Footer } from './components/Footer';

function App() {
  return (
    <Router>
      <div className="App">
        <header className="header">
          <h1>Registro de Actividades Axiliares</h1>
        </header>
        <Navbar />
        <div className="container">
          {/* Definición de Rutas */}
          <Routes>
            <Route path="/" element={<HomePage />} />
            <Route path="/actividad" element={<ActividadList />} />
            <Route path="/actividad/nueva" element={<ActividadForm />} />
            <Route path="/actividad/:id" element={<ActividadDetail />} />
            <Route path="/actividad/editar/:id" element={<ActividadDetail />} />
          </Routes>
        </div>
      </div>
      <Footer />
    </Router>
  );
}

export default App;