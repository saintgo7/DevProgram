import 'package:flutter/material.dart';

void main() => runApp(const App095());

class App095 extends StatelessWidget {
  const App095({Key? key}) : super(key: key);

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'Advanced App 095',
      theme: ThemeData(
        primarySwatch: Colors.deepPurple,
        visualDensity: VisualDensity.adaptivePlatformDensity,
      ),
      home: const AdvancedPage(),
    );
  }
}

class AdvancedPage extends StatefulWidget {
  const AdvancedPage({Key? key}) : super(key: key);

  @override
  State<AdvancedPage> createState() => _AdvancedPageState();
}

class _AdvancedPageState extends State<AdvancedPage>
    with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  late Animation<double> _animation;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(
      duration: const Duration(seconds: 2),
      vsync: this,
    )..repeat(reverse: true);
    _animation = Tween<double>(begin: 0, end: 1).animate(_controller);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
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
  }
}
