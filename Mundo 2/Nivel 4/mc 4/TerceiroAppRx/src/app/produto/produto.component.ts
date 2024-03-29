import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { Produto } from '../produto';
import { ProdutoService } from '../produto.service';

@Component({
    selector: 'app-produto',
    templateUrl: './produto.component.html',
    styleUrls: ['./produto.component.css']
})
export class ProdutoComponent implements OnInit {
    router: Router;
    servProd: ProdutoService;
    produtos: Array<Produto> = [];
    constructor(router: Router, servProd: ProdutoService) {
        this.router = router;
        this.servProd = servProd;
    }
    incluir(): void { this.router.navigateByUrl("/novoprod"); }
    private obterTodos() {
        this.servProd.obterTodos()
            .subscribe((produtos) => this.produtos = produtos);
    }
    excluir(id: number): void {
        this.servProd.remover(id).subscribe(_ => this.obterTodos());
    }
    ngOnInit(): void { this.obterTodos(); }
}
