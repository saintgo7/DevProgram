import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="counter-app">
      <h1>Counter App</h1>
      <div class="counter-display">
        <p>Counter Value:</p>
        <h2>{{ count }}</h2>
      </div>
      <div class="button-group">
        <button (click)="decrement()">-</button>
        <button (click)="reset()" class="reset">Reset</button>
        <button (click)="increment()">+</button>
      </div>
    </div>
  `,
  styles: [`
    .counter-app {
      text-align: center;
      padding: 50px;
    }

    .counter-display h2 {
      font-size: 48px;
      color: #dd0031;
      margin: 20px 0;
    }

    .button-group {
      display: flex;
      gap: 15px;
      justify-content: center;
    }

    button {
      padding: 10px 30px;
      font-size: 18px;
      border: none;
      border-radius: 5px;
      background-color: #dd0031;
      color: white;
      cursor: pointer;
    }

    button.reset {
      background-color: #e74c3c;
    }

    button:hover {
      opacity: 0.8;
    }
  `]
})
export class AppComponent {
  count = 0;

  increment(): void {
    this.count++;
  }

  decrement(): void {
    this.count--;
  }

  reset(): void {
    this.count = 0;
  }
}
