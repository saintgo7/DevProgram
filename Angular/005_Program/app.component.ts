import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="binding-demo">
      <h1>Data Binding Demo</h1>

      <!-- Interpolation -->
      <h2>{{ title }}</h2>

      <!-- Property Binding -->
      <input [value]="inputValue" readonly />

      <!-- Two-way Binding -->
      <input [(ngModel)]="twoWayValue" />
      <p>Two-way value: {{ twoWayValue }}</p>

      <!-- Event Binding -->
      <button (click)="onClick()">Click Count: {{ clickCount }}</button>

      <!-- Class Binding -->
      <div [class.active]="isActive" class="status-box">
        {{ isActive ? 'Active' : 'Inactive' }}
      </div>
      <button (click)="toggleActive()">Toggle Status</button>
    </div>
  `,
  styles: [`
    .binding-demo {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
    }

    input {
      display: block;
      width: 100%;
      padding: 10px;
      margin: 10px 0;
      border: 1px solid #ddd;
      border-radius: 5px;
    }

    button {
      padding: 10px 20px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      margin: 10px 0;
    }

    .status-box {
      padding: 20px;
      margin: 20px 0;
      border-radius: 5px;
      text-align: center;
      background-color: #f5f5f5;
    }

    .status-box.active {
      background-color: #4caf50;
      color: white;
    }
  `]
})
export class AppComponent {
  title = 'Data Binding Examples';
  inputValue = 'Property Binding Value';
  twoWayValue = 'Edit me!';
  clickCount = 0;
  isActive = false;

  onClick(): void {
    this.clickCount++;
  }

  toggleActive(): void {
    this.isActive = !this.isActive;
  }
}
