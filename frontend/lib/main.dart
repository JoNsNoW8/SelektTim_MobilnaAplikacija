import 'package:flutter/material.dart';

import 'widgets/navbar.dart';

void main() {
  runApp(
    MaterialApp(
      title: 'Selekt tim',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: const HomePage(),
    ),
  );
}

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    return const Navbar();
  }
}
