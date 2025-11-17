import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormsModule } from '@angular/forms';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="todo-app">
      <h1>Todo List</h1>
      <div class="input-group">
        <input
          [(ngModel)]="newTodo"
          (keyup.enter)="addTodo()"
          placeholder="Enter a task"
        />
        <button (click)="addTodo()">Add</button>
      </div>
      <ul class="todo-list">
        <li *ngFor="let todo of todos; let i = index">
          <span>{{ todo }}</span>
          <button (click)="removeTodo(i)" class="delete">✕</button>
        </li>
      </ul>
      <p *ngIf="todos.length === 0" class="empty-message">
        No tasks yet. Add one above!
      </p>
    </div>
  `,
  styles: [`
    .todo-app {
      max-width: 500px;
      margin: 50px auto;
      padding: 20px;
    }

    .input-group {
      display: flex;
      gap: 10px;
      margin-bottom: 20px;
    }

    input {
      flex: 1;
      padding: 10px;
      font-size: 16px;
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

    .todo-list {
      list-style: none;
      padding: 0;
    }

    .todo-list li {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 10px;
      margin: 5px 0;
      background-color: #f5f5f5;
      border-radius: 5px;
    }

    .delete {
      background-color: #e74c3c;
      padding: 5px 10px;
    }

    .empty-message {
      text-align: center;
      color: #999;
    }
  `]
})
export class AppComponent {
  newTodo = '';
  todos: string[] = [];

  addTodo(): void {
    if (this.newTodo.trim()) {
      this.todos.push(this.newTodo);
      this.newTodo = '';
    }
  }

  removeTodo(index: number): void {
    this.todos.splice(index, 1);
  }
}
