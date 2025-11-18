import 'dart:io';

class TodoItem {
  String task;
  bool completed;

  TodoItem(this.task, {this.completed = false});

  @override
  String toString() => completed ? '[✓] $task' : '[ ] $task';
}

class TodoList {
  List<TodoItem> items = [];

  void addTask(String task) {
    items.add(TodoItem(task));
    print('Added: $task');
  }

  void completeTask(int index) {
    if (index >= 0 && index < items.length) {
      items[index].completed = true;
      print('Completed: ${items[index].task}');
    }
  }

  void displayTasks() {
    if (items.isEmpty) {
      print('No tasks yet!');
      return;
    }

    print('\n=== Todo List ===');
    for (int i = 0; i < items.length; i++) {
      print('$i. ${items[i]}');
    }
  }
}

void main() {
  TodoList todoList = TodoList();

  while (true) {
    print('\n1. Add Task');
    print('2. Complete Task');
    print('3. View Tasks');
    print('4. Exit');
    stdout.write('Choose option: ');

    String? choice = stdin.readLineSync();

    switch (choice) {
      case '1':
        stdout.write('Enter task: ');
        String? task = stdin.readLineSync();
        if (task != null && task.isNotEmpty) {
          todoList.addTask(task);
        }
        break;
      case '2':
        stdout.write('Task number to complete: ');
        int index = int.parse(stdin.readLineSync()!);
        todoList.completeTask(index);
        break;
      case '3':
        todoList.displayTasks();
        break;
      case '4':
        print('Goodbye!');
        return;
    }
  }
}
