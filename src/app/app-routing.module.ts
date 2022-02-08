import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import {RouterModule, Routes} from '@angular/router';
import { HomeComponent } from './home/home.component';
import {ChicagoComponent} from './chicago/chicago.component';
import {LaComponent} from './la/la.component';
import {PhillyComponent} from './philly/philly.component';

const routes: Routes = [
  {path: 'home', component: HomeComponent},
  {path: 'chicago', component: ChicagoComponent},
  {path: 'la', component: LaComponent},
  {path: 'philly', component: PhillyComponent},
  { path: '', redirectTo: '/home', pathMatch: 'full' }
]

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
