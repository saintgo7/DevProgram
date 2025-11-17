import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  template: `
    <div class="app">
      <h1>Angular Program {{ programNumber }}</h1>
      <p>{{ message }}</p>
      <button (click)="updateMessage()">Click Me</button>
    </div>
  `,
  styles: [`
    .app {
      text-align: center;
      padding: 50px;
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
  programNumber = 014;
  message = 'Basic Angular component';

  updateMessage(): void {
    this.message = 'Button clicked!';
  }
}
