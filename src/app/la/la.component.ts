import { Component, OnInit } from '@angular/core';
import {QueryService} from '../query.service';
import {Event} from '../models';

@Component({
  selector: 'app-la',
  templateUrl: './la.component.html',
  styleUrls: ['./la.component.css']
})
export class LaComponent implements OnInit {

  displayedColumns: any;
  dataSource: any;
  eventList: Array<Event> = new Array<Event>();

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.eventList = this.getLAEvents();
    this.buildTable();
  }

  public buildTable(): void {
    let dC: string[] = ['name', 'venue', 'link', 'time'];
    let source = this.getLAEvents();
    this.displayedColumns = dC;
    this.dataSource = source;
  }

  public getLAEvents(): Array<Event> {
    let events = this.queryService.importLA();
    let other = new Array<Event>();
    if (events !== undefined) {
      return events;
    } else { return other }
  }

}
