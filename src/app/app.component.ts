import { Component } from '@angular/core';
import data from '../assets/data.json';
import { OnInit } from '@angular/core';
import {HttpClient} from "@angular/common/http";
import { Observable } from 'rxjs';
import { QueryService } from './query.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'event-tracker';

  // data: Array<any> = this.queryService.chicago;
  // var res;
  // resp: any = data;
  constructor(
              //private queryService: QueryService
              ) {
//     this.getJSON().subscribe(data => {
//         console.log(data['chicago'][0]['name']);
//         // res = data;
//     });
     //this.printJSON()
  }

}
// var json = require('./assets/data.json');
