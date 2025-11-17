import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="state-demo">
      <h1>State Management {{ programNumber }}</h1>
      <p>Count: {{ count }}</p>
      <p>Status: {{ isActive ? 'Active' : 'Inactive' }}</p>
      <button (click)="toggleActive()">Toggle</button>
      <button (click)="increment()">Increment</button>
    </div>
  `,
  styles: [`
    .state-demo {
      text-align: center;
      padding: 50px;
    }

    button {
      margin: 5px;
      padding: 10px 20px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }
  `]
})
export class AppComponent {
  programNumber = 024;
  count = 0;
  isActive = false;

  toggleActive(): void {
    this.isActive = !this.isActive;
  }

  increment(): void {
    this.count++;
  }

  get doubledCount(): number {
    return this.count * 2;
  }
}
