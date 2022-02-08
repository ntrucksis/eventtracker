import { ComponentFixture, TestBed } from '@angular/core/testing';

import { PhillyComponent } from './philly.component';

describe('PhillyComponent', () => {
  let component: PhillyComponent;
  let fixture: ComponentFixture<PhillyComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ PhillyComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(PhillyComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
