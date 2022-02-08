import { Component, OnInit } from '@angular/core';
import { QueryService } from '../query.service';
import { Event } from '../models';
import {MatTableModule} from '@angular/material/table';

@Component({
  selector: 'app-chicago',
  templateUrl: './chicago.component.html',
  styleUrls: ['./chicago.component.css']
})
export class ChicagoComponent implements OnInit {

  displayedColumns: any;
  dataSource: any;
  eventList: Array<Event> = new Array<Event>();

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.eventList = this.getChiEvents();
    this.buildTable();
  }

  public buildTable(): void {
    let dC: string[] = ['name', 'venue', 'link', 'time'];
    let source = this.getChiEvents();
    this.displayedColumns = dC;
    this.dataSource = source;
  }

  public getChiEvents(): Array<Event> {
    let events = this.queryService.importChicago();
    let other = new Array<Event>();
    if (events !== undefined) {
      return events
    } else { return other }
  }

}
