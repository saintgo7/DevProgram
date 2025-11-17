import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="services-demo">
      <h1>Services Demo {{ programNumber }}</h1>
      <input [(ngModel)]="newItem" placeholder="Enter item" />
      <button (click)="addItem()">Add Item</button>
      <ul>
        <li *ngFor="let item of items">{{ item }}</li>
      </ul>
    </div>
  `,
  styles: [`
    .services-demo {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
    }

    input {
      padding: 10px;
      margin-right: 10px;
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
    }

    ul {
      list-style: none;
      padding: 0;
      margin-top: 20px;
    }

    li {
      padding: 10px;
      margin: 5px 0;
      background-color: #f5f5f5;
      border-radius: 5px;
    }
  `]
})
export class AppComponent {
  programNumber = 073;
  newItem = '';
  items: string[] = [];

  addItem(): void {
    if (this.newItem.trim()) {
      this.items.push(this.newItem);
      this.newItem = '';
    }
  }
}
