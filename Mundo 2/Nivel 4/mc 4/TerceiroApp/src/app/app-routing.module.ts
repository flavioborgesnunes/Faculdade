import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { NovProdComponent } from './nov-prod/nov-prod.component';
import { ProdutoComponent } from './produto/produto.component';
import { LoginService } from './login.service';
import { LoginComponent } from './login/login.component';

const routes: Routes = [
  { path: 'home', component: HomeComponent },
  { path: 'login', component: LoginComponent },
  { path: 'produto', component: ProdutoComponent, 
  canActivate: [LoginService] },
  { path: 'novoprod', component: NovProdComponent, 
  canActivate: [LoginService] },
  { path: '', redirectTo: '/home', pathMatch: 'full' },
 ];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
