import React from "react";
import ControleEditora from "./controle/ControleEditora";
import ControleLivro from "./controle/ControleLivros"

const listaDeLivros =  new ControleLivro().obterLivro();
const controleEditora = new ControleEditora();


function LivroLista() {
    return(
        <>
           <table className="table table-striped">
            <thead className= "thead-dark">
                <th>Titulo</th>
                <th>Resumo</th>
                <th>Editora</th>
                <th>Autores</th>
            </thead>
            <tbody>
                {listaDeLivros.map((livro, index)=> (

                
                <tr>
                    <th scope="col">
                        <h5>{livro.titulo}</h5>
                        <button>Excluir</button>
                    </th>
                    <th scope="col">
                        <p>{livro.resumo}</p>
                    </th>
                    <th scope="col">
                        <p>{livro.codEditora}</p>
                    </th>
                    <th>
                        <ul>
                            {livro.autores.map((autor) =>
                                <li>{autor}</li>
                                )}
                        </ul>
                    </th>
                </tr>
                ) )}
            </tbody>
           </table>
        </>
    )
}
export default LivroLista;