import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  standalone: true,
  template: `
    <div class="app">
      <h1>{{ message }}</h1>
      <p>{{ subtitle }}</p>
    </div>
  `,
  styles: [`
    .app {
      text-align: center;
      padding: 50px;
    }

    h1 {
      color: #dd0031;
    }
  `]
})
export class AppComponent {
  message = 'Hello, Angular!';
  subtitle = 'Welcome to Angular Programming';
}
