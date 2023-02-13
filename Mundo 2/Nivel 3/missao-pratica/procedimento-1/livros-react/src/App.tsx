import React from 'react';
import './App.css';
import LivroLista from './LivroLista';

function App() {
  document.title = 'Livros React'
  return (
    <div className="App">
      <LivroLista/>
    </div>
  );
}

export default App;
