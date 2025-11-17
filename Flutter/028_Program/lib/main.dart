import 'package:flutter/material.dart';

void main() => runApp(const App028());

class App028 extends StatelessWidget {
  const App028({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'State Management 028',
      home: const StatefulPage(),
    );
  }
}

class StatefulPage extends StatefulWidget {
  const StatefulPage({Key? key}) : super(key: key);

  @override
  State<StatefulPage> createState() => _StatefulPageState();
}

class _StatefulPageState extends State<StatefulPage> {
  bool _isActive = false;

  @override
  Widget build(BuildContext context) {
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
              onPressed: () {
                setState(() {
                  _isActive = !_isActive;
                });
              },
              child: const Text('Toggle State'),
            ),
          ],
        ),
      ),
    );
  }
}
