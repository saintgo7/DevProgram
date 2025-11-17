import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

interface FormData {
  name: string;
  email: string;
  message: string;
}

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="form-app">
      <h1>Form Input Demo</h1>
      <form (ngSubmit)="handleSubmit()">
        <div class="form-group">
          <label>Name:</label>
          <input [(ngModel)]="formData.name" name="name" type="text" required />
        </div>
        <div class="form-group">
          <label>Email:</label>
          <input [(ngModel)]="formData.email" name="email" type="email" required />
        </div>
        <div class="form-group">
          <label>Message:</label>
          <textarea [(ngModel)]="formData.message" name="message" rows="4"></textarea>
        </div>
        <button type="submit">Submit</button>
      </form>
      <div *ngIf="submitted" class="result">
        <h3>Submitted Data:</h3>
        <p><strong>Name:</strong> {{ formData.name }}</p>
        <p><strong>Email:</strong> {{ formData.email }}</p>
        <p><strong>Message:</strong> {{ formData.message }}</p>
      </div>
    </div>
  `,
  styles: [`
    .form-app {
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
    }

    .form-group {
      margin-bottom: 20px;
    }

    label {
      display: block;
      margin-bottom: 5px;
      font-weight: bold;
    }

    input, textarea {
      width: 100%;
      padding: 10px;
      font-size: 16px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }

    button {
      padding: 10px 30px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
      font-size: 16px;
    }

    .result {
      margin-top: 30px;
      padding: 20px;
      background-color: #e8f5e9;
      border-radius: 5px;
    }
  `]
})
export class AppComponent {
  formData: FormData = {
    name: '',
    email: '',
    message: ''
  };
  submitted = false;

  handleSubmit(): void {
    this.submitted = true;
    setTimeout(() => {
      this.submitted = false;
    }, 5000);
  }
}
