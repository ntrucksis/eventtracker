import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import {Event} from './models'
import data from '../assets/data.json';

@Injectable({
  providedIn: 'root'
})
export class QueryService {

  constructor(private http: HttpClient) {}

  public importChicago(): Array<Event> {
    let event_array: Array<Event> = new Array<Event>();
    for (let i=0; i<data.chicago.length; i++) {
     let e_time: string = data.chicago[i].time;
     if (e_time == "DATE TBA") {
       continue;
     }
     let real_time: Date = this.getTimeRight(e_time);
     let ev: Event = {
       name: data.chicago[i].name,
       venue: data.chicago[i].venue,
       link: data.chicago[i].link,
       time: real_time
     }
     event_array.push(ev);
    }
    this.sortByDate(event_array);
    return event_array;
  }

  public importLA(): Array<Event> {
    let event_array: Array<Event> = new Array<Event>();
    for (let i=0; i<data['los-angeles'].length; i++) {
      let e_time: string = data['los-angeles'][i].time;
      if (e_time == "DATE TBA") {
        continue;
      }
      let real_time: Date = this.getTimeRight(e_time);
      let ev: Event = {
        name: data['los-angeles'][i].name,
        venue: data['los-angeles'][i].venue,
        link: data['los-angeles'][i].link,
        time: real_time
      }
      event_array.push(ev);
    }
    this.sortByDate(event_array);
    return event_array;
  }

  public importPhilly(): Array<Event> {
    let event_array: Array<Event> = new Array<Event>();
    for (let i=0; i<data['philly'].length; i++) {
      let e_time: string = data.philly[i].time;
      if (e_time == "DATE TBA") {
        continue;
      }
      let real_time: Date = this.getTimeRight(e_time);
      let ev: Event = {
        name: data.philly[i].name,
        venue: data.philly[i].venue,
        link: data.philly[i].link,
        time: real_time
      }
      event_array.push(ev);
    }
    this.sortByDate(event_array);
    return event_array;
  }

  public getTimeRight(time: string): Date {
    let oldTime = time;
    let monthDay = oldTime.slice(4, -14);
    let year = oldTime.slice(20);
    const realTime = "" + monthDay + " " + year;
    const dateTime = new Date(realTime);
    return dateTime;
  }

  public sortByDate(arr: Array<Event>): void {
    arr.sort(function(a,b) {
      return a.time.getTime() - b.time.getTime();
    });
  }

   public getJSON(): Observable<any> {
       return this.http.get<JSON>("./assets/data.json");
   }
}
