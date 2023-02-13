import Livro from "../modelo/Livro"

var livros: Array<Livro> = [
    {
        codigo:1,
        codEditora: 1,
        titulo: 'livro1',
        resumo: 'Será que funciona?',
        autores: ['autor1','autor2']
    },
    {
        codigo:2,
        codEditora: 2,
        titulo: 'livro2',
        resumo: 'Qualquer',
        autores: ['autor3','autor4']
    },
    {
        codigo:3,
        codEditora: 3,
        titulo: 'livro3',
        resumo: 'Qualquer',
        autores: ['autor5','autor6']
    },
]

export default class ControleLivro {

    obterLivro(){
        return livros
    }
    incluir(livro:Livro){
        livro =  livros[(-1)+1];
    }
    excluir(num:Number){
        function valorIgual(){
            if(num === livros.length){
                livros.splice(0)
            }
            
        }
        livros.findIndex(valorIgual)
    }
}