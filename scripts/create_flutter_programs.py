#!/usr/bin/env python3
"""
Create 100 Flutter/Dart programs
"""

import os
import json

base_dir = "/home/user/DevProgram/Flutter"

# Flutter program templates
flutter_programs = {
    1: ("Hello World App", "Simple Flutter hello world", """import 'package:flutter/material.dart';

void main() {
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Hello World',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    );
  }
}

class HomePage extends StatelessWidget {
  const HomePage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Hello World App'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: const [
            Text(
              'Hello, Flutter!',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold),
            ),
            SizedBox(height: 20),
            Text(
              'Welcome to Flutter Development',
              style: TextStyle(fontSize: 16),
            ),
          ],
        ),
      ),
    );
  }
}
"""),

    2: ("Counter App", "Simple counter application", """import 'package:flutter/material.dart';

void main() => runApp(const CounterApp());

class CounterApp extends StatelessWidget {
  const CounterApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Counter App',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const CounterPage(),
    );
  }
}

class CounterPage extends StatefulWidget {
  const CounterPage({Key? key}) : super(key: key);

  @override
  State<CounterPage> createState() => _CounterPageState();
}

class _CounterPageState extends State<CounterPage> {
  int _counter = 0;

  void _incrementCounter() {
    setState(() {
      _counter++;
    });
  }

  void _decrementCounter() {
    setState(() {
      _counter--;
    });
  }

  void _resetCounter() {
    setState(() {
      _counter = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Counter App'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            const Text(
              'Counter Value:',
              style: TextStyle(fontSize: 20),
            ),
            Text(
              '$_counter',
              style: Theme.of(context).textTheme.headline1,
            ),
            const SizedBox(height: 30),
            Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                ElevatedButton(
                  onPressed: _decrementCounter,
                  child: const Icon(Icons.remove),
                ),
                const SizedBox(width: 20),
                ElevatedButton(
                  onPressed: _resetCounter,
                  child: const Text('Reset'),
                ),
                const SizedBox(width: 20),
                ElevatedButton(
                  onPressed: _incrementCounter,
                  child: const Icon(Icons.add),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }
}
"""),

    3: ("Text Input App", "Text input and display", """import 'package:flutter/material.dart';

void main() => runApp(const TextInputApp());

class TextInputApp extends StatelessWidget {
  const TextInputApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Text Input App',
      home: const TextInputPage(),
    );
  }
}

class TextInputPage extends StatefulWidget {
  const TextInputPage({Key? key}) : super(key: key);

  @override
  State<TextInputPage> createState() => _TextInputPageState();
}

class _TextInputPageState extends State<TextInputPage> {
  final _textController = TextEditingController();
  String _displayText = '';

  @override
  void dispose() {
    _textController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('Text Input App'),
      ),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _textController,
              decoration: const InputDecoration(
                labelText: 'Enter text',
                border: OutlineInputBorder(),
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                setState(() {
                  _displayText = _textController.text;
                });
              },
              child: const Text('Submit'),
            ),
            const SizedBox(height: 20),
            Text(
              _displayText,
              style: const TextStyle(fontSize: 20),
            ),
          ],
        ),
      ),
    );
  }
}
"""),

    4: ("List View App", "Scrollable list demonstration", """import 'package:flutter/material.dart';

void main() => runApp(const ListViewApp());

class ListViewApp extends StatelessWidget {
  const ListViewApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'ListView App',
      home: const ListViewPage(),
    );
  }
}

class ListViewPage extends StatelessWidget {
  const ListViewPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    final items = List<String>.generate(50, (i) => 'Item ${i + 1}');

    return Scaffold(
      appBar: AppBar(
        title: const Text('ListView Example'),
      ),
      body: ListView.builder(
        itemCount: items.length,
        itemBuilder: (context, index) {
          return ListTile(
            leading: CircleAvatar(
              child: Text('${index + 1}'),
            ),
            title: Text(items[index]),
            subtitle: Text('Subtitle for item ${index + 1}'),
            trailing: const Icon(Icons.arrow_forward_ios),
            onTap: () {
              ScaffoldMessenger.of(context).showSnackBar(
                SnackBar(content: Text('Tapped on ${items[index]}')),
              );
            },
          );
        },
      ),
    );
  }
}
"""),

    5: ("GridView App", "Grid layout demonstration", """import 'package:flutter/material.dart';

void main() => runApp(const GridViewApp());

class GridViewApp extends StatelessWidget {
  const GridViewApp({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'GridView App',
      home: const GridViewPage(),
    );
  }
}

class GridViewPage extends StatelessWidget {
  const GridViewPage({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text('GridView Example'),
      ),
      body: GridView.builder(
        padding: const EdgeInsets.all(10),
        gridDelegate: const SliverGridDelegateWithFixedCrossAxisCount(
          crossAxisCount: 2,
          crossAxisSpacing: 10,
          mainAxisSpacing: 10,
        ),
        itemCount: 20,
        itemBuilder: (context, index) {
          return Card(
            color: Colors.blue[(index % 9 + 1) * 100],
            child: Center(
              child: Text(
                'Item ${index + 1}',
                style: const TextStyle(
                  color: Colors.white,
                  fontSize: 20,
                ),
              ),
            ),
          );
        },
      ),
    );
  }
}
"""),
}

# Generate remaining programs
for i in range(6, 101):
    if i <= 20:
        # Basic Widgets
        template = f"""import 'package:flutter/material.dart';

void main() => runApp(const App{i:03d}());

class App{i:03d} extends StatelessWidget {{
  const App{i:03d}({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      title: 'Flutter App {i:03d}',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const HomePage(),
    );
  }}
}}

class HomePage extends StatelessWidget {{
  const HomePage({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(
        title: const Text('Basic Widget Demo'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: const [
            Icon(Icons.flutter_dash, size: 100, color: Colors.blue),
            SizedBox(height: 20),
            Text('Flutter Program {i:03d}', style: TextStyle(fontSize: 24)),
          ],
        ),
      ),
    );
  }}
}}
"""
    elif i <= 40:
        # State Management
        template = f"""import 'package:flutter/material.dart';

void main() => runApp(const App{i:03d}());

class App{i:03d} extends StatelessWidget {{
  const App{i:03d}({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      title: 'State Management {i:03d}',
      home: const StatefulPage(),
    );
  }}
}}

class StatefulPage extends StatefulWidget {{
  const StatefulPage({{Key? key}}) : super(key: key);

  @override
  State<StatefulPage> createState() => _StatefulPageState();
}}

class _StatefulPageState extends State<StatefulPage> {{
  bool _isActive = false;

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(
        title: const Text('State Management Demo'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Text(
              _isActive ? 'Active' : 'Inactive',
              style: TextStyle(
                fontSize: 32,
                color: _isActive ? Colors.green : Colors.red,
              ),
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {{
                setState(() {{
                  _isActive = !_isActive;
                }});
              }},
              child: const Text('Toggle State'),
            ),
          ],
        ),
      ),
    );
  }}
}}
"""
    elif i <= 60:
        # Navigation
        template = f"""import 'package:flutter/material.dart';

void main() => runApp(const App{i:03d}());

class App{i:03d} extends StatelessWidget {{
  const App{i:03d}({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      title: 'Navigation {i:03d}',
      home: const FirstPage(),
    );
  }}
}}

class FirstPage extends StatelessWidget {{
  const FirstPage({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(
        title: const Text('First Page'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {{
            Navigator.push(
              context,
              MaterialPageRoute(builder: (context) => const SecondPage()),
            );
          }},
          child: const Text('Go to Second Page'),
        ),
      ),
    );
  }}
}}

class SecondPage extends StatelessWidget {{
  const SecondPage({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(
        title: const Text('Second Page'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {{
            Navigator.pop(context);
          }},
          child: const Text('Go Back'),
        ),
      ),
    );
  }}
}}
"""
    elif i <= 80:
        # Data & Forms
        template = f"""import 'package:flutter/material.dart';

void main() => runApp(const App{i:03d}());

class App{i:03d} extends StatelessWidget {{
  const App{i:03d}({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      title: 'Data App {i:03d}',
      home: const DataPage(),
    );
  }}
}}

class DataPage extends StatefulWidget {{
  const DataPage({{Key? key}}) : super(key: key);

  @override
  State<DataPage> createState() => _DataPageState();
}}

class _DataPageState extends State<DataPage> {{
  final List<String> _items = [];
  final _controller = TextEditingController();

  @override
  void dispose() {{
    _controller.dispose();
    super.dispose();
  }}

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(
        title: const Text('Data Management'),
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(8.0),
            child: Row(
              children: [
                Expanded(
                  child: TextField(
                    controller: _controller,
                    decoration: const InputDecoration(
                      hintText: 'Enter item',
                    ),
                  ),
                ),
                IconButton(
                  icon: const Icon(Icons.add),
                  onPressed: () {{
                    if (_controller.text.isNotEmpty) {{
                      setState(() {{
                        _items.add(_controller.text);
                        _controller.clear();
                      }});
                    }}
                  }},
                ),
              ],
            ),
          ),
          Expanded(
            child: ListView.builder(
              itemCount: _items.length,
              itemBuilder: (context, index) {{
                return ListTile(
                  title: Text(_items[index]),
                  trailing: IconButton(
                    icon: const Icon(Icons.delete),
                    onPressed: () {{
                      setState(() {{
                        _items.removeAt(index);
                      }});
                    }},
                  ),
                );
              }},
            ),
          ),
        ],
      ),
    );
  }}
}}
"""
    else:
        # Advanced Features
        template = f"""import 'package:flutter/material.dart';

void main() => runApp(const App{i:03d}());

class App{i:03d} extends StatelessWidget {{
  const App{i:03d}({{Key? key}}) : super(key: key);

  @override
  Widget build(BuildContext context) {{
    return MaterialApp(
      title: 'Advanced App {i:03d}',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const AdvancedPage(),
    );
  }}
}}

class AdvancedPage extends StatefulWidget {{
  const AdvancedPage({{Key? key}}) : super(key: key);

  @override
  State<AdvancedPage> createState() => _AdvancedPageState();
}}

class _AdvancedPageState extends State<AdvancedPage>
    with SingleTickerProviderStateMixin {{
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {{
    super.initState();
    _controller = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    )..repeat(reverse: true);
    _animation = Tween<double>(begin: 0, end: 1).animate(_controller);
  }}

  @override
  void dispose() {{
    _controller.dispose();
    super.dispose();
  }}

  @override
  Widget build(BuildContext context) {{
    return Scaffold(
      appBar: AppBar(
        title: const Text('Advanced Features'),
      ),
      body: Center(
        child: FadeTransition(
          opacity: _animation,
          child: const Icon(
            Icons.star,
            size: 100,
            color: Colors.amber,
          ),
        ),
      ),
    );
  }}
}}
"""

    flutter_programs[i] = (f"Program {i}", f"Flutter program {i}", template)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in flutter_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(f"{program_dir}/lib", exist_ok=True)

    # Write main.dart
    with open(f"{program_dir}/lib/main.dart", 'w') as f:
        f.write(code)

    # Create pubspec.yaml
    pubspec = f"""name: flutter_program_{num:03d}
description: {desc}
version: 1.0.0

environment:
  sdk: '>=2.18.0 <3.0.0'

dependencies:
  flutter:
    sdk: flutter
  cupertino_icons: ^1.0.2

dev_dependencies:
  flutter_test:
    sdk: flutter
  flutter_lints: ^2.0.0

flutter:
  uses-material-design: true
"""
    with open(f"{program_dir}/pubspec.yaml", 'w') as f:
        f.write(pubspec)

    print(f"Created: {num:03d} - {title}")

print(f"\\nCreated {len(flutter_programs)} Flutter programs in {base_dir}")
