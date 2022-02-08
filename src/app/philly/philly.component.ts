import { Component, OnInit } from '@angular/core';
import {QueryService} from '../query.service';
import {Event} from '../models';

@Component({
  selector: 'app-philly',
  templateUrl: './philly.component.html',
  styleUrls: ['./philly.component.css']
})
export class PhillyComponent implements OnInit {
  displayedColumns: any;
  dataSource: any;
  eventList: Array<Event> = new Array<Event>();

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.eventList = this.getPhillyEvents();
    this.buildTable();
  }

  public buildTable(): void {
    let dC: string[] = ['name', 'venue', 'link', 'time'];
    let source = this.getPhillyEvents();
    this.displayedColumns = dC;
    this.dataSource = source;
  }

  public getPhillyEvents(): Array<Event> {
    let events = this.queryService.importPhilly();
    let other = new Array<Event>();
    if (events !== undefined) {
      return events;
    } else {return other }
  }

}
