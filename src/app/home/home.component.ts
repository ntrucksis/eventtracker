import { Component, OnInit } from '@angular/core';
import { QueryService } from '../query.service';
import {Event} from '../models';
import {MatButtonModule} from '@angular/material/button';
import {MatIconModule} from '@angular/material/icon';

@Component({
  selector: 'app-home',
  templateUrl: './home.component.html',
  styleUrls: ['./home.component.css']
})
export class HomeComponent implements OnInit {
  displayedColumns:any;
  dataSource:any;

  events: Array<Event> = new Array<Event>();
  thisMonthEvents: Array<Event> = new Array<Event>();

  constructor(private queryService: QueryService) { }

  ngOnInit(): void {
    this.events = this.getEvents();
    this.thisMonthEvents = this.last30Days(this.events);
    this.buildTable();
  }

  public getEvents(): Array<Event> {
    let chi_events = this.queryService.importChicago();
    let la_events = this.queryService.importLA();
    let ph_events = this.queryService.importPhilly();
    let LA = la_events.concat(ph_events);
    let all_events = chi_events.concat(LA);
    this.queryService.sortByDate(all_events);
    return all_events;
  }

  public last30Days(events: Array<Event>): Array<Event> {
    let newDate = new Date();
    newDate.setDate(newDate.getDate() + 30);
    let index: Array<number> = new Array<number>();
    let idx = 0;
    console.log(newDate);
    for (let i=0; i < events.length; i++) {
      if (events[i].time.getTime() - newDate.getTime() >= 0) {
          idx = i;
          break;
      }
    }
    events.splice(idx);
    return events;
  }

  public buildTable(): void {
    let dC: string[] = ['name', 'venue', 'link', 'time'];
    let source = this.thisMonthEvents;
    this.displayedColumns = dC;
    this.dataSource = source;
  }



}
