import  Editora from "../modelo/Editora";

var editoras: Array<Editora> =[
    {
        nomeEditora : "editora1",
        codEditora : 1
    },
    {
        nomeEditora : "editora2",
        codEditora : 2
    },
    {
        nomeEditora : "editora3",
        codEditora : 3
    }
];

export default class ControleEditora {
    getNomeEditora(codEditora : Number){
        return editoras.filter((editoras)=> {return editoras.nomeEditora})
    };
    getEditoras(){
        return editoras;
    };
}
