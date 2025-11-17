import { Component, OnInit, OnDestroy } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="advanced-demo">
      <h1>Advanced Features {{ programNumber }}</h1>
      <p *ngIf="show">{{ message }}</p>
      <button (click)="toggle()">Toggle</button>
      <div class="counter">
        <p>Timer: {{ timer }}</p>
      </div>
    </div>
  `,
  styles: [`
    .advanced-demo {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
    }

    button {
      padding: 10px 20px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }

    .counter {
      margin-top: 20px;
      padding: 20px;
      background-color: #f5f5f5;
      border-radius: 5px;
      text-align: center;
    }
  `]
})
export class AppComponent implements OnInit, OnDestroy {
  programNumber = 091;
  message = 'This is an advanced Angular component';
  show = true;
  timer = 0;
  private intervalId: any;

  ngOnInit(): void {
    this.intervalId = setInterval(() => {
      this.timer++;
    }, 1000);
  }

  ngOnDestroy(): void {
    if (this.intervalId) {
      clearInterval(this.intervalId);
    }
  }

  toggle(): void {
    this.show = !this.show;
  }
}
