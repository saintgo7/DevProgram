import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="directives-demo">
      <h1>Directives Demo {{ programNumber }}</h1>
      <ul>
        <li *ngFor="let item of items; let i = index">
          Item {{ i + 1 }}: {{ item | uppercase }}
        </li>
      </ul>
      <p *ngIf="showMessage">This message is conditionally displayed</p>
      <button (click)="toggleMessage()">Toggle Message</button>
    </div>
  `,
  styles: [`
    .directives-demo {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
    }

    ul {
      list-style: none;
      padding: 0;
    }

    li {
      padding: 10px;
      margin: 5px 0;
      background-color: #f5f5f5;
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
  `]
})
export class AppComponent {
  programNumber = 052;
  items = ['apple', 'banana', 'cherry', 'date', 'elderberry'];
  showMessage = true;

  toggleMessage(): void {
    this.showMessage = !this.showMessage;
  }
}
