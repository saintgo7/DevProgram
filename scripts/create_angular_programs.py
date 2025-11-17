#!/usr/bin/env python3
"""
Create 100 Angular programs
"""

import os
import json

base_dir = "/home/user/DevProgram/Angular"

# Angular program templates
angular_programs = {
    1: ("Hello World", "Basic Angular hello world", """import { Component } from '@angular/core';

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
"""),

    2: ("Counter App", "Counter with increment/decrement", """import { Component } from '@angular/core';
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
"""),

    3: ("Todo List", "Angular todo list", """import { Component } from '@angular/core';
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
"""),

    4: ("Form Input", "Angular form handling", """import { Component } from '@angular/core';
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
"""),

    5: ("Data Binding", "Angular data binding examples", """import { Component } from '@angular/core';
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
"""),
}

# Generate remaining programs (6-100)
for i in range(6, 101):
    if i <= 20:
        # Basic Components
        code = f"""import {{ Component }} from '@angular/core';

@Component({{
  selector: 'app-root',
  standalone: true,
  template: `
    <div class="app">
      <h1>Angular Program {{{{ programNumber }}}}</h1>
      <p>{{{{ message }}}}</p>
      <button (click)="updateMessage()">Click Me</button>
    </div>
  `,
  styles: [`
    .app {{
      text-align: center;
      padding: 50px;
    }}

    button {{
      padding: 10px 20px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }}
  `]
}})
export class AppComponent {{
  programNumber = {i:03d};
  message = 'Basic Angular component';

  updateMessage(): void {{
    this.message = 'Button clicked!';
  }}
}}
"""
    elif i <= 40:
        # State Management
        code = f"""import {{ Component }} from '@angular/core';
import {{ CommonModule }} from '@angular/common';

@Component({{
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="state-demo">
      <h1>State Management {{{{ programNumber }}}}</h1>
      <p>Count: {{{{ count }}}}</p>
      <p>Status: {{{{ isActive ? 'Active' : 'Inactive' }}}}</p>
      <button (click)="toggleActive()">Toggle</button>
      <button (click)="increment()">Increment</button>
    </div>
  `,
  styles: [`
    .state-demo {{
      text-align: center;
      padding: 50px;
    }}

    button {{
      margin: 5px;
      padding: 10px 20px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }}
  `]
}})
export class AppComponent {{
  programNumber = {i:03d};
  count = 0;
  isActive = false;

  toggleActive(): void {{
    this.isActive = !this.isActive;
  }}

  increment(): void {{
    this.count++;
  }}

  get doubledCount(): number {{
    return this.count * 2;
  }}
}}
"""
    elif i <= 60:
        # Directives and Pipes
        code = f"""import {{ Component }} from '@angular/core';
import {{ CommonModule }} from '@angular/common';

@Component({{
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="directives-demo">
      <h1>Directives Demo {{{{ programNumber }}}}</h1>
      <ul>
        <li *ngFor="let item of items; let i = index">
          Item {{{{ i + 1 }}}}: {{{{ item | uppercase }}}}
        </li>
      </ul>
      <p *ngIf="showMessage">This message is conditionally displayed</p>
      <button (click)="toggleMessage()">Toggle Message</button>
    </div>
  `,
  styles: [`
    .directives-demo {{
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
    }}

    ul {{
      list-style: none;
      padding: 0;
    }}

    li {{
      padding: 10px;
      margin: 5px 0;
      background-color: #f5f5f5;
      border-radius: 5px;
    }}

    button {{
      padding: 10px 20px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }}
  `]
}})
export class AppComponent {{
  programNumber = {i:03d};
  items = ['apple', 'banana', 'cherry', 'date', 'elderberry'];
  showMessage = true;

  toggleMessage(): void {{
    this.showMessage = !this.showMessage;
  }}
}}
"""
    elif i <= 80:
        # Services and Dependency Injection
        code = f"""import {{ Component }} from '@angular/core';
import {{ CommonModule }} from '@angular/common';
import {{ FormsModule }} from '@angular/forms';

@Component({{
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, FormsModule],
  template: `
    <div class="services-demo">
      <h1>Services Demo {{{{ programNumber }}}}</h1>
      <input [(ngModel)]="newItem" placeholder="Enter item" />
      <button (click)="addItem()">Add Item</button>
      <ul>
        <li *ngFor="let item of items">{{{{ item }}}}</li>
      </ul>
    </div>
  `,
  styles: [`
    .services-demo {{
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
    }}

    input {{
      padding: 10px;
      margin-right: 10px;
      border: 1px solid #ddd;
      border-radius: 5px;
    }}

    button {{
      padding: 10px 20px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }}

    ul {{
      list-style: none;
      padding: 0;
      margin-top: 20px;
    }}

    li {{
      padding: 10px;
      margin: 5px 0;
      background-color: #f5f5f5;
      border-radius: 5px;
    }}
  `]
}})
export class AppComponent {{
  programNumber = {i:03d};
  newItem = '';
  items: string[] = [];

  addItem(): void {{
    if (this.newItem.trim()) {{
      this.items.push(this.newItem);
      this.newItem = '';
    }}
  }}
}}
"""
    else:
        # Advanced Features
        code = f"""import {{ Component, OnInit, OnDestroy }} from '@angular/core';
import {{ CommonModule }} from '@angular/common';

@Component({{
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule],
  template: `
    <div class="advanced-demo">
      <h1>Advanced Features {{{{ programNumber }}}}</h1>
      <p *ngIf="show">{{{{ message }}}}</p>
      <button (click)="toggle()">Toggle</button>
      <div class="counter">
        <p>Timer: {{{{ timer }}}}</p>
      </div>
    </div>
  `,
  styles: [`
    .advanced-demo {{
      max-width: 600px;
      margin: 50px auto;
      padding: 20px;
    }}

    button {{
      padding: 10px 20px;
      background-color: #dd0031;
      color: white;
      border: none;
      border-radius: 5px;
      cursor: pointer;
    }}

    .counter {{
      margin-top: 20px;
      padding: 20px;
      background-color: #f5f5f5;
      border-radius: 5px;
      text-align: center;
    }}
  `]
}})
export class AppComponent implements OnInit, OnDestroy {{
  programNumber = {i:03d};
  message = 'This is an advanced Angular component';
  show = true;
  timer = 0;
  private intervalId: any;

  ngOnInit(): void {{
    this.intervalId = setInterval(() => {{
      this.timer++;
    }}, 1000);
  }}

  ngOnDestroy(): void {{
    if (this.intervalId) {{
      clearInterval(this.intervalId);
    }}
  }}

  toggle(): void {{
    this.show = !this.show;
  }}
}}
"""

    angular_programs[i] = (f"Program {i}", f"Angular program {i}", code)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in angular_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write app.component.ts
    with open(f"{program_dir}/app.component.ts", 'w') as f:
        f.write(code)

    # Create package.json
    package_json = {
        "name": f"angular-program-{num:03d}",
        "version": "1.0.0",
        "description": desc,
        "scripts": {
            "ng": "ng",
            "start": "ng serve",
            "build": "ng build",
            "watch": "ng build --watch",
            "test": "ng test"
        },
        "private": True,
        "dependencies": {
            "@angular/animations": "^17.0.0",
            "@angular/common": "^17.0.0",
            "@angular/compiler": "^17.0.0",
            "@angular/core": "^17.0.0",
            "@angular/forms": "^17.0.0",
            "@angular/platform-browser": "^17.0.0",
            "@angular/platform-browser-dynamic": "^17.0.0",
            "rxjs": "~7.8.0",
            "tslib": "^2.3.0",
            "zone.js": "~0.14.2"
        },
        "devDependencies": {
            "@angular-devkit/build-angular": "^17.0.0",
            "@angular/cli": "^17.0.0",
            "@angular/compiler-cli": "^17.0.0",
            "typescript": "~5.2.2"
        }
    }

    with open(f"{program_dir}/package.json", 'w') as f:
        json.dump(package_json, f, indent=2)

    # Create tsconfig.json
    tsconfig = {
        "compilerOptions": {
            "target": "ES2022",
            "module": "ES2022",
            "lib": ["ES2022", "dom"],
            "strict": True,
            "esModuleInterop": True,
            "skipLibCheck": True,
            "experimentalDecorators": True
        }
    }

    with open(f"{program_dir}/tsconfig.json", 'w') as f:
        json.dump(tsconfig, f, indent=2)

    print(f"Created: {num:03d} - {title}")

print(f"\nCreated {len(angular_programs)} Angular programs in {base_dir}")
