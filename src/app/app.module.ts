import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import {HttpClientModule} from '@angular/common/http';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';
import { AppComponent } from './app.component';
import { HomeComponent } from './home/home.component';
import { AppRoutingModule } from './app-routing.module';
import { ChicagoComponent } from './chicago/chicago.component';
import {MatTableModule} from '@angular/material/table';
import { LaComponent } from './la/la.component';
import { PhillyComponent } from './philly/philly.component';


@NgModule({
  declarations: [
    AppComponent,
    HomeComponent,
    ChicagoComponent,
    LaComponent,
    PhillyComponent,
  ],
  imports: [
    BrowserModule,
    HttpClientModule,
    MatButtonModule,
    MatIconModule,
    AppRoutingModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
