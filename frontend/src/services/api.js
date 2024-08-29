import axios from 'axios';

const API_URL = 'http://127.0.0.1:8000/docs#/';  // Cambia la URL si es necesario

export const api = axios.create({
  baseURL: API_URL,
});