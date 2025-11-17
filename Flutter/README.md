# Flutter/Dart Programs Collection

**100 Production-Ready Flutter/Dart Programs**

A comprehensive collection of Flutter mobile and web application examples demonstrating Material Design, state management, navigation patterns, and modern Flutter development practices.

---

## 📊 Overview

| Metric | Value |
|--------|-------|
| **Total Programs** | 100 |
| **Total Lines** | ~6,392 |
| **Avg Lines/Program** | ~63.9 |
| **Language** | Dart |
| **Framework** | Flutter |
| **Flutter Version** | 2.18.0+ |
| **Dart SDK** | >=2.18.0 <3.0.0 |

---

## 🗂️ Repository Structure

```
Flutter/
├── README.md                    # This file
├── 001_Program/                 # Hello World App
│   ├── lib/
│   │   └── main.dart           # Main application code
│   └── pubspec.yaml            # Package configuration
├── 002_Program/                 # Counter App
├── 003_Program/                 # Text Input App
├── 004_Program/                 # List View App
├── 005_Program/                 # GridView App
├── ...
└── 100_Program/                 # Advanced Features
```

---

## 🚀 Quick Start

### Prerequisites

**Required:**
- Flutter SDK 2.18.0 or higher
- Dart SDK >=2.18.0 <3.0.0
- Android Studio / VS Code with Flutter extensions
- For web: Chrome browser
- For mobile: Android SDK / Xcode

**Installation:**

```bash
# Install Flutter SDK
# Download from: https://flutter.dev/docs/get-started/install

# Verify installation
flutter --version
dart --version

# Check for any issues
flutter doctor
```

### Running a Program

```bash
# Navigate to a program directory
cd Flutter/001_Program

# Get dependencies
flutter pub get

# Run on connected device/emulator
flutter run

# Run on web
flutter run -d chrome

# Run on specific device
flutter devices              # List available devices
flutter run -d <device-id>   # Run on specific device
```

### Building for Production

```bash
# Build APK (Android)
flutter build apk

# Build App Bundle (Android)
flutter build appbundle

# Build iOS (requires macOS)
flutter build ios

# Build Web
flutter build web

# Build for all platforms
flutter build apk && flutter build web
```

---

## 📚 Program Categories

### **001-020: Basic Widgets** (20 programs)
Fundamental Flutter widgets and Material Design components

**Featured Programs:**
- **001_Program**: Hello World App - Basic Flutter app structure
- **002_Program**: Counter App - StatefulWidget with state management
- **003_Program**: Text Input App - TextField and form handling
- **004_Program**: List View App - Scrollable lists with ListView.builder
- **005_Program**: GridView App - Grid layouts with GridView.builder
- **006-020**: Basic widget demonstrations (Icon, Text, Container, Column, Row, etc.)

**Key Concepts:**
- Material Design
- StatelessWidget
- Basic layouts
- Widget composition
- Theme configuration

### **021-040: State Management** (20 programs)
State handling patterns and reactive UI updates

**Key Concepts:**
- StatefulWidget
- setState() method
- State lifecycle
- Toggle switches
- Dynamic UI updates
- Boolean state management

**Example Pattern:**
```dart
class StatefulPage extends StatefulWidget {
  @override
  State<StatefulPage> createState() => _StatefulPageState();
}

class _StatefulPageState extends State<StatefulPage> {
  bool _isActive = false;

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: ElevatedButton(
        onPressed: () {
          setState(() {
            _isActive = !_isActive;
          });
        },
        child: Text(_isActive ? 'Active' : 'Inactive'),
      ),
    );
  }
}
```

### **041-060: Navigation** (20 programs)
Screen navigation and routing patterns

**Key Concepts:**
- Navigator.push()
- Navigator.pop()
- MaterialPageRoute
- Route transitions
- Passing data between screens
- Navigation stack management

**Example Pattern:**
```dart
// Navigate to second page
Navigator.push(
  context,
  MaterialPageRoute(builder: (context) => const SecondPage()),
);

// Go back
Navigator.pop(context);

// Pop with result
Navigator.pop(context, resultData);
```

### **061-080: Data & Forms** (20 programs)
Data management, forms, and user input handling

**Key Concepts:**
- TextEditingController
- Form validation
- List management
- CRUD operations
- TextField widgets
- Dynamic list updates

**Example Pattern:**
```dart
class DataPage extends StatefulWidget {
  @override
  State<DataPage> createState() => _DataPageState();
}

class _DataPageState extends State<DataPage> {
  final List<String> _items = [];
  final _controller = TextEditingController();

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _addItem() {
    setState(() {
      _items.add(_controller.text);
      _controller.clear();
    });
  }

  // ... build method with ListView
}
```

### **081-100: Advanced Features** (20 programs)
Animations, advanced patterns, and complex UI

**Key Concepts:**
- AnimationController
- Tween animations
- FadeTransition
- SingleTickerProviderStateMixin
- Custom animations
- Visual effects

**Example Pattern:**
```dart
class AdvancedPage extends StatefulWidget {
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

  // ... build with FadeTransition
}
```

---

## 💡 Key Features

### Flutter Best Practices

✅ **Material Design**
- Consistent Material Design components
- Theme configuration
- primarySwatch color schemes
- Responsive layouts

✅ **Widget Patterns**
- StatelessWidget for static content
- StatefulWidget for dynamic content
- Proper widget composition
- Const constructors for performance

✅ **State Management**
- setState() for local state
- Proper state lifecycle
- Memory leak prevention
- Controller disposal

✅ **Resource Management**
- TextEditingController disposal
- AnimationController disposal
- Proper dispose() overrides
- Memory-efficient widgets

✅ **Code Organization**
- Separation of concerns
- Widget extraction
- Clear naming conventions
- Type safety with Dart

### All Programs Feature:

- **Independent Execution**: Each program runs standalone
- **Material Design**: Google's design system
- **Hot Reload**: Fast development iterations
- **Cross-Platform**: Run on iOS, Android, Web, Desktop
- **Type Safety**: Strong typing with Dart
- **Production-Ready**: Enterprise-grade code quality

---

## 🎯 Learning Path

### Beginner (Programs 001-020)
**Focus**: Basic widgets and layouts

1. **001_Program**: Understand Flutter app structure
2. **002_Program**: Learn StatefulWidget and setState
3. **003_Program**: Handle user input with TextField
4. **004_Program**: Create scrollable lists
5. **005_Program**: Build grid layouts

**Skills Learned:**
- Flutter project structure
- Material Design basics
- Widget tree composition
- Basic state management
- Layout widgets

### Intermediate (Programs 021-060)
**Focus**: State management and navigation

**State Management (021-040):**
- Complex state handling
- Multiple state variables
- Reactive UI updates
- Toggle patterns

**Navigation (041-060):**
- Multi-screen apps
- Route navigation
- Data passing
- Back navigation

**Skills Learned:**
- Advanced state patterns
- Navigation stack
- Route management
- Screen transitions

### Advanced (Programs 061-100)
**Focus**: Data handling and animations

**Data & Forms (061-080):**
- Form validation
- List management
- CRUD operations
- Controller patterns

**Advanced Features (081-100):**
- Custom animations
- Animation controllers
- Visual effects
- Performance optimization

**Skills Learned:**
- Animation API
- Tween animations
- Controller lifecycle
- Advanced patterns

---

## 🛠️ Development Environment

### Recommended IDEs

**Android Studio** (Recommended)
- Full Flutter support
- Emulator management
- Hot reload/restart
- Widget inspector

**Visual Studio Code**
- Lightweight and fast
- Flutter extension
- Dart extension
- Excellent debugging

**IntelliJ IDEA**
- JetBrains IDE
- Flutter plugin
- Advanced refactoring
- Professional features

### Essential Extensions

**VS Code:**
- Flutter (Dart-Code.flutter)
- Dart (Dart-Code.dart-code)
- Flutter Widget Snippets
- Awesome Flutter Snippets

**Android Studio:**
- Flutter plugin
- Dart plugin

### Useful Commands

```bash
# Create new Flutter project
flutter create project_name

# Run app
flutter run

# Hot reload (press 'r' during run)
# Hot restart (press 'R' during run)

# Analyze code
flutter analyze

# Format code
dart format .

# Run tests
flutter test

# Clean build files
flutter clean

# Update dependencies
flutter pub get

# Upgrade packages
flutter pub upgrade

# Check for updates
flutter upgrade
```

---

## 📖 Flutter Concepts

### Widget Tree

Everything in Flutter is a widget:

```dart
MaterialApp
└─ Scaffold
   ├─ AppBar
   │  └─ Text
   └─ Body
      └─ Center
         └─ Column
            ├─ Text
            └─ ElevatedButton
```

### Stateless vs Stateful

**StatelessWidget:**
- Immutable
- Cannot change once built
- Good for static content

**StatefulWidget:**
- Mutable
- Can rebuild with new data
- Has State object

### Lifecycle Methods

```dart
// StatefulWidget lifecycle
initState()      // Called once when widget is created
build()          // Called every time widget rebuilds
setState()       // Triggers rebuild
dispose()        // Called when widget is removed
```

---

## 🔧 Common Issues & Solutions

### Issue: "Failed to build for Android"

**Solution:**
```bash
# Update Gradle
cd android && ./gradlew clean
cd .. && flutter clean
flutter pub get
flutter run
```

### Issue: "Waiting for another flutter command to release the startup lock"

**Solution:**
```bash
# Kill Flutter process
killall -9 dart
rm -rf /path/to/flutter/bin/cache/lockfile

# Or delete the lock file manually
```

### Issue: "Hot reload not working"

**Solution:**
- Press 'R' for hot restart instead of 'r'
- Make sure changes are saved
- Check for syntax errors
- Try `flutter clean && flutter run`

### Issue: "Version solving failed"

**Solution:**
```bash
# Clear pub cache
flutter pub cache repair

# Update dependencies
flutter pub upgrade

# Clean and reinstall
flutter clean
flutter pub get
```

---

## 📊 Performance Tips

### Optimization Strategies

1. **Use const constructors**
   ```dart
   const Text('Hello')  // Better than Text('Hello')
   ```

2. **Extract widgets**
   ```dart
   // Extract repeated widgets into separate classes
   class MyCustomWidget extends StatelessWidget { }
   ```

3. **Avoid rebuilding expensive widgets**
   ```dart
   // Use keys to preserve state
   ListView(key: PageStorageKey('list'))
   ```

4. **Use ListView.builder for large lists**
   ```dart
   ListView.builder(
     itemCount: items.length,
     itemBuilder: (context, index) => ListTile(...)
   )
   ```

5. **Profile your app**
   ```bash
   flutter run --profile
   # Use DevTools for performance profiling
   ```

---

## 🌐 Deployment

### Android Deployment

```bash
# Build release APK
flutter build apk --release

# Build App Bundle (recommended for Play Store)
flutter build appbundle --release

# Output location:
# build/app/outputs/flutter-apk/app-release.apk
# build/app/outputs/bundle/release/app-release.aab
```

### iOS Deployment (macOS only)

```bash
# Build iOS release
flutter build ios --release

# Open in Xcode for signing and deployment
open ios/Runner.xcworkspace
```

### Web Deployment

```bash
# Build web release
flutter build web

# Output location: build/web/
# Deploy to Firebase Hosting, Netlify, etc.
```

---

## 📚 Additional Resources

### Official Documentation
- [Flutter Documentation](https://flutter.dev/docs)
- [Dart Documentation](https://dart.dev/guides)
- [Flutter API Reference](https://api.flutter.dev/)
- [Material Design](https://material.io/design)

### Learning Resources
- [Flutter Codelabs](https://flutter.dev/docs/codelabs)
- [Flutter YouTube Channel](https://www.youtube.com/c/flutterdev)
- [Dart Language Tour](https://dart.dev/guides/language/language-tour)
- [Flutter Cookbook](https://flutter.dev/docs/cookbook)

### Community
- [Flutter Community](https://flutter.dev/community)
- [Stack Overflow - Flutter](https://stackoverflow.com/questions/tagged/flutter)
- [Reddit - r/FlutterDev](https://www.reddit.com/r/FlutterDev/)
- [Flutter Discord](https://discord.gg/flutter)

### Tools & Packages
- [pub.dev](https://pub.dev/) - Dart package repository
- [Flutter DevTools](https://flutter.dev/docs/development/tools/devtools)
- [Firebase for Flutter](https://firebase.google.com/docs/flutter)

---

## 🎯 Program Index

### Quick Reference

| Range | Category | Description |
|-------|----------|-------------|
| 001-005 | Featured Apps | Complete implementations with full features |
| 006-020 | Basic Widgets | Fundamental widget demonstrations |
| 021-040 | State Management | State handling patterns |
| 041-060 | Navigation | Screen navigation and routing |
| 061-080 | Data & Forms | Data management and forms |
| 081-100 | Advanced | Animations and advanced features |

### Featured Programs Detail

1. **001_Program** - Hello World App
   - Basic app structure
   - Material Design theme
   - Scaffold and AppBar

2. **002_Program** - Counter App
   - StatefulWidget
   - Multiple buttons (increment, decrement, reset)
   - setState pattern

3. **003_Program** - Text Input App
   - TextEditingController
   - TextField widget
   - User input handling

4. **004_Program** - List View App
   - ListView.builder
   - ListTile widgets
   - SnackBar notifications

5. **005_Program** - GridView App
   - GridView.builder
   - Grid layouts
   - Dynamic colors

---

## 💻 Example: Building Your First App

### Step-by-Step Guide

```bash
# 1. Navigate to a program
cd Flutter/001_Program

# 2. Install dependencies
flutter pub get

# 3. List available devices
flutter devices

# 4. Run on web
flutter run -d chrome

# 5. Or run on mobile emulator
flutter run -d emulator-5554
```

### Modifying a Program

1. Open `lib/main.dart` in your IDE
2. Make changes (e.g., change text, colors)
3. Save the file
4. Press 'r' in terminal for hot reload
5. See changes instantly!

---

## 🔍 Code Quality

### Best Practices Implemented

✅ **Dart Conventions**
- lowerCamelCase for variables
- UpperCamelCase for classes
- Const constructors where possible
- Type annotations

✅ **Flutter Patterns**
- Proper widget composition
- State management
- Resource disposal
- Material Design

✅ **Documentation**
- Clear class names
- Descriptive widget names
- Comments where needed

✅ **Performance**
- Const constructors
- Efficient builders
- Proper key usage
- Memory management

---

## 📈 Project Statistics

**Created**: 2025-11-17
**Framework**: Flutter
**Language**: Dart
**Total Programs**: 100
**Total Code Lines**: ~6,392
**Average Lines/Program**: ~63.9
**Complexity Range**: Beginner to Advanced
**Platform Support**: Android, iOS, Web, Desktop

---

**Happy Flutter Development! 🚀**

For questions or issues, refer to the main repository CLAUDE.md file or consult the official Flutter documentation.
