import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ChicagoComponent } from './chicago.component';

describe('ChicagoComponent', () => {
  let component: ChicagoComponent;
  let fixture: ComponentFixture<ChicagoComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ChicagoComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(ChicagoComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
