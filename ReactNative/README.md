# React Native Programs Collection

**100 Production-Ready React Native Programs**

A comprehensive collection of React Native mobile application examples demonstrating cross-platform development, component patterns, state management, and modern React Native best practices.

---

## 📊 Overview

| Metric | Value |
|--------|-------|
| **Total Programs** | 100 |
| **Total Lines** | ~8,049 |
| **Avg Lines/Program** | ~80.5 |
| **Language** | TypeScript/JavaScript |
| **Framework** | React Native |
| **React Native Version** | 0.72.0 |
| **React Version** | 18.2.0 |

---

## 🗂️ Repository Structure

```
ReactNative/
├── README.md                    # This file
├── 001_Program/                 # Hello World App
│   ├── App.tsx                  # Main application code
│   ├── package.json             # Package configuration
│   └── tsconfig.json            # TypeScript configuration
├── 002_Program/                 # Counter App
├── 003_Program/                 # Text Input App
├── 004_Program/                 # FlatList App
├── 005_Program/                 # Todo List App
├── ...
└── 100_Program/                 # Advanced Features
```

---

## 🚀 Quick Start

### Prerequisites

**Required:**
- Node.js 16+ (LTS recommended)
- npm or yarn
- React Native CLI (`npm install -g react-native-cli`)
- For iOS: Xcode 12+ (macOS only)
- For Android: Android Studio with SDK

**Installation:**

```bash
# Install React Native CLI globally
npm install -g react-native-cli

# Or use npx (no global installation needed)
npx react-native --version

# Check React Native environment
npx react-native doctor
```

### Running a Program

```bash
# Navigate to a program directory
cd ReactNative/001_Program

# Install dependencies
npm install
# or
yarn install

# Run on iOS (macOS only)
npx react-native run-ios

# Run on Android
npx react-native run-android

# Start Metro bundler separately
npx react-native start
```

### iOS Specific Setup

```bash
# Install CocoaPods dependencies (iOS only)
cd ios
pod install
cd ..

# Run on specific iOS device
npx react-native run-ios --device "iPhone 14"

# Run on simulator
npx react-native run-ios --simulator="iPhone 14 Pro"
```

### Android Specific Setup

```bash
# List available Android devices/emulators
adb devices

# Run on specific device
npx react-native run-android --deviceId=<device-id>

# Build release APK
cd android
./gradlew assembleRelease
```

---

## 📚 Program Categories

### **001-020: Basic Components** (20 programs)
Fundamental React Native components and UI patterns

**Featured Programs:**
- **001_Program**: Hello World App - Basic React Native app structure
- **002_Program**: Counter App - useState hook with increment/decrement
- **003_Program**: Text Input App - TextInput and form handling
- **004_Program**: FlatList App - Scrollable lists with FlatList
- **005_Program**: Todo List App - CRUD operations with local state
- **006-020**: Basic component demonstrations

**Key Concepts:**
- SafeAreaView
- View, Text, TouchableOpacity
- StyleSheet
- Basic layouts (flexbox)
- Event handling

### **021-040: State Management** (20 programs)
React hooks and state handling patterns

**Key Concepts:**
- useState hook
- useEffect hook
- Component lifecycle
- State updates and re-renders
- Conditional rendering
- Multiple state variables

**Example Pattern:**
```typescript
import React, {useState, useEffect} from 'react';

const App = () => {
  const [count, setCount] = useState(0);
  const [isActive, setIsActive] = useState(false);

  useEffect(() => {
    console.log('Component mounted');
    return () => console.log('Component unmounted');
  }, []);

  return (
    <View>
      <Text>{count}</Text>
      <Button onPress={() => setCount(count + 1)} title="Increment" />
    </View>
  );
};
```

### **041-060: Navigation** (20 programs)
Screen navigation patterns (simplified without navigation library)

**Key Concepts:**
- Screen transitions
- State-based navigation
- Passing data between screens
- Navigation patterns
- Back navigation

**Example Pattern:**
```typescript
const App = () => {
  const [currentScreen, setCurrentScreen] = useState('home');

  return (
    <SafeAreaView>
      {currentScreen === 'home' ? (
        <HomeScreen onNavigate={() => setCurrentScreen('details')} />
      ) : (
        <DetailsScreen onGoBack={() => setCurrentScreen('home')} />
      )}
    </SafeAreaView>
  );
};
```

**Note:** For production apps, use React Navigation library for advanced routing.

### **061-080: Forms & Input** (20 programs)
Form handling, validation, and user input

**Key Concepts:**
- TextInput component
- Form state management
- Input validation
- Multi-field forms
- Keyboard handling
- ScrollView for forms

**Example Pattern:**
```typescript
const App = () => {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
  });

  const handleSubmit = () => {
    if (formData.name && formData.email) {
      // Process form
      console.log('Form submitted:', formData);
    }
  };

  return (
    <ScrollView>
      <TextInput
        value={formData.name}
        onChangeText={text => setFormData({...formData, name: text})}
        placeholder="Name"
      />
      {/* More inputs */}
      <Button onPress={handleSubmit} title="Submit" />
    </ScrollView>
  );
};
```

### **081-100: Advanced Features** (20 programs)
Animations, advanced patterns, and optimizations

**Key Concepts:**
- Animated API
- Animated.Value
- Animated.timing
- Animated.sequence
- Animated.loop
- FadeIn/FadeOut animations
- useNativeDriver for performance

**Example Pattern:**
```typescript
const App = () => {
  const [fadeAnim] = useState(new Animated.Value(0));

  useEffect(() => {
    Animated.loop(
      Animated.sequence([
        Animated.timing(fadeAnim, {
          toValue: 1,
          duration: 1000,
          useNativeDriver: true,
        }),
        Animated.timing(fadeAnim, {
          toValue: 0,
          duration: 1000,
          useNativeDriver: true,
        }),
      ])
    ).start();
  }, []);

  return (
    <Animated.View style={{opacity: fadeAnim}}>
      <Text>Fading Animation</Text>
    </Animated.View>
  );
};
```

---

## 💡 Key Features

### React Native Best Practices

✅ **TypeScript Integration**
- Strong typing for props and state
- Type-safe component definitions
- Interface-based design
- Better IDE support

✅ **Component Patterns**
- Functional components
- React Hooks (useState, useEffect)
- Proper prop handling
- Component composition

✅ **Styling**
- StyleSheet for performance
- Flexbox layouts
- Platform-specific styles
- Responsive design patterns

✅ **Performance**
- useNativeDriver for animations
- FlatList for long lists
- Proper key props
- Memoization where needed

✅ **Cross-Platform**
- iOS and Android support
- Platform-agnostic code
- Native performance
- Single codebase

### All Programs Feature:

- **Independent Execution**: Each program runs standalone
- **TypeScript**: Type-safe development
- **Modern Hooks**: useState, useEffect patterns
- **Responsive UI**: Flexbox layouts
- **Performance**: Optimized rendering
- **Production-Ready**: Enterprise-grade code quality

---

## 🎯 Learning Path

### Beginner (Programs 001-020)
**Focus**: Basic components and layouts

1. **001_Program**: Understand React Native app structure
2. **002_Program**: Learn useState hook and state management
3. **003_Program**: Handle user input with TextInput
4. **004_Program**: Create scrollable lists with FlatList
5. **005_Program**: Build a simple Todo app with CRUD operations

**Skills Learned:**
- React Native project structure
- JSX syntax
- Component hierarchy
- Basic styling with StyleSheet
- Event handling
- State management basics

### Intermediate (Programs 021-060)
**Focus**: State management and navigation

**State Management (021-040):**
- Complex state with multiple variables
- useEffect for side effects
- Component lifecycle
- Conditional rendering

**Navigation (041-060):**
- Screen transitions
- State-based routing
- Data passing
- Back navigation

**Skills Learned:**
- Advanced React hooks
- State management patterns
- Navigation concepts
- Component communication

### Advanced (Programs 061-100)
**Focus**: Forms and animations

**Forms & Input (061-080):**
- Multi-field forms
- Form validation
- Input handling
- ScrollView usage

**Advanced Features (081-100):**
- Animated API
- Custom animations
- Performance optimization
- Advanced patterns

**Skills Learned:**
- Animation API
- Performance techniques
- Advanced React patterns
- Production-ready code

---

## 🛠️ Development Environment

### Recommended IDEs

**Visual Studio Code** (Recommended)
- React Native Tools extension
- TypeScript support
- ESLint integration
- IntelliSense

**WebStorm / IntelliJ IDEA**
- Built-in React Native support
- Advanced refactoring
- Professional features

### Essential Extensions (VS Code)

- **React Native Tools** - Microsoft's official extension
- **ES7+ React/Redux/React-Native snippets** - Code snippets
- **Prettier** - Code formatter
- **ESLint** - Linting
- **Auto Import** - Automatic imports

### Useful Commands

```bash
# Start Metro bundler
npx react-native start

# Clear Metro cache
npx react-native start --reset-cache

# Run on iOS
npx react-native run-ios

# Run on Android
npx react-native run-android

# List iOS devices
xcrun simctl list devices

# List Android devices
adb devices

# Debug menu (iOS Simulator)
Cmd + D

# Debug menu (Android Emulator)
Cmd + M (or Ctrl + M on Windows/Linux)

# Reload app
Press R twice (or Cmd/Ctrl + R)

# Enable hot reloading
Shake device or press Cmd/Ctrl + D → Enable Hot Reloading
```

---

## 📖 React Native Concepts

### Component Structure

```typescript
import React from 'react';
import {View, Text, StyleSheet} from 'react-native';

const MyComponent = () => {
  return (
    <View style={styles.container}>
      <Text style={styles.text}>Hello</Text>
    </View>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  text: {
    fontSize: 20,
  },
});

export default MyComponent;
```

### Core Components

- **View**: Container component (like `div`)
- **Text**: Text display (like `span` or `p`)
- **Image**: Image display
- **TextInput**: Text input field
- **ScrollView**: Scrollable container
- **FlatList**: Performant list for large datasets
- **TouchableOpacity**: Touchable component with opacity feedback
- **Button**: Basic button component
- **SafeAreaView**: Safe area for notched devices

### Styling with StyleSheet

```typescript
const styles = StyleSheet.create({
  container: {
    flex: 1,                    // Flexbox
    backgroundColor: '#fff',    // Background
    padding: 20,                // Spacing
  },
  text: {
    fontSize: 18,               // Typography
    fontWeight: 'bold',
    color: '#333',
  },
});
```

### Flexbox Layout

React Native uses Flexbox for layouts:

```typescript
{
  flexDirection: 'row',        // or 'column' (default)
  justifyContent: 'center',    // Main axis alignment
  alignItems: 'center',        // Cross axis alignment
  flex: 1,                     // Flex grow
}
```

---

## 🔧 Common Issues & Solutions

### Issue: Metro bundler port in use

**Solution:**
```bash
# Kill process on port 8081
lsof -ti:8081 | xargs kill

# Or start on different port
npx react-native start --port 8088
```

### Issue: Build failed on iOS

**Solution:**
```bash
# Clean iOS build
cd ios
rm -rf build
rm -rf Pods
rm Podfile.lock
pod install
cd ..

# Then rebuild
npx react-native run-ios
```

### Issue: Build failed on Android

**Solution:**
```bash
# Clean Android build
cd android
./gradlew clean
cd ..

# Clear Metro cache
npx react-native start --reset-cache

# Rebuild
npx react-native run-android
```

### Issue: "Unable to resolve module"

**Solution:**
```bash
# Clear npm cache
npm cache clean --force

# Delete node_modules and reinstall
rm -rf node_modules
npm install

# Reset Metro
npx react-native start --reset-cache
```

### Issue: "Command PhaseScriptExecution failed" (iOS)

**Solution:**
```bash
cd ios
pod deintegrate
pod install
cd ..
```

---

## 📊 Performance Tips

### Optimization Strategies

1. **Use FlatList for large lists**
   ```typescript
   <FlatList
     data={items}
     renderItem={({item}) => <Item {...item} />}
     keyExtractor={item => item.id}
     removeClippedSubviews={true}  // Performance boost
   />
   ```

2. **Enable useNativeDriver**
   ```typescript
   Animated.timing(animValue, {
     toValue: 1,
     duration: 300,
     useNativeDriver: true,  // Runs on native thread
   })
   ```

3. **Memoize components**
   ```typescript
   import React, {memo} from 'react';

   const MyComponent = memo(({data}) => {
     return <View>...</View>;
   });
   ```

4. **Use React.useMemo for expensive calculations**
   ```typescript
   const expensiveValue = useMemo(() => {
     return computeExpensiveValue(data);
   }, [data]);
   ```

5. **Avoid inline functions in render**
   ```typescript
   // Bad
   <Button onPress={() => handlePress(item)} />

   // Good
   const handleItemPress = useCallback(() => handlePress(item), [item]);
   <Button onPress={handleItemPress} />
   ```

---

## 🌐 Deployment

### iOS Deployment

```bash
# Build for iOS
cd ios
xcodebuild -workspace MyApp.xcworkspace \
  -scheme MyApp \
  -configuration Release \
  -archivePath MyApp.xcarchive \
  archive

# Or use Xcode
# Open ios/MyApp.xcworkspace
# Product → Archive
```

### Android Deployment

```bash
# Build release APK
cd android
./gradlew assembleRelease

# Output: android/app/build/outputs/apk/release/app-release.apk

# Build App Bundle (for Play Store)
./gradlew bundleRelease

# Output: android/app/build/outputs/bundle/release/app-release.aab
```

### Code Signing

**iOS:**
- Configure signing in Xcode
- Requires Apple Developer account
- Set up provisioning profiles

**Android:**
- Generate keystore
- Configure gradle.properties
- Sign APK/AAB

---

## 📚 Additional Resources

### Official Documentation
- [React Native Documentation](https://reactnative.dev/docs/getting-started)
- [React Documentation](https://react.dev/)
- [TypeScript Documentation](https://www.typescriptlang.org/docs/)
- [Expo Documentation](https://docs.expo.dev/) (alternative framework)

### Learning Resources
- [React Native Tutorial](https://reactnative.dev/docs/tutorial)
- [React Native Express](https://www.reactnative.express/)
- [Awesome React Native](https://github.com/jondot/awesome-react-native)
- [React Native School](https://www.reactnativeschool.com/)

### Community
- [React Native Community](https://github.com/react-native-community)
- [Stack Overflow - React Native](https://stackoverflow.com/questions/tagged/react-native)
- [Reddit - r/reactnative](https://www.reddit.com/r/reactnative/)
- [Discord - Reactiflux](https://www.reactiflux.com/)

### Popular Libraries
- [React Navigation](https://reactnavigation.org/) - Routing and navigation
- [Redux](https://redux.js.org/) - State management
- [React Native Paper](https://reactnativepaper.com/) - Material Design
- [React Native Elements](https://reactnativeelements.com/) - UI toolkit
- [Reanimated](https://docs.swmansion.com/react-native-reanimated/) - Advanced animations

---

## 🎯 Program Index

### Quick Reference

| Range | Category | Description |
|-------|----------|-------------|
| 001-005 | Featured Apps | Complete implementations with full features |
| 006-020 | Basic Components | Fundamental component demonstrations |
| 021-040 | State Management | React hooks and state patterns |
| 041-060 | Navigation | Screen navigation patterns |
| 061-080 | Forms & Input | Form handling and validation |
| 081-100 | Advanced | Animations and advanced features |

### Featured Programs Detail

1. **001_Program** - Hello World App
   - Basic app structure
   - SafeAreaView and View
   - Text styling

2. **002_Program** - Counter App
   - useState hook
   - Multiple buttons (increment, decrement, reset)
   - Event handling

3. **003_Program** - Text Input App
   - TextInput component
   - State updates
   - User input handling

4. **004_Program** - FlatList App
   - FlatList for scrollable lists
   - renderItem callback
   - TouchableOpacity feedback

5. **005_Program** - Todo List App
   - CRUD operations
   - Array state management
   - Dynamic list rendering

---

## 💻 Example: Building Your First App

### Step-by-Step Guide

```bash
# 1. Navigate to a program
cd ReactNative/001_Program

# 2. Install dependencies
npm install

# 3. Start Metro bundler
npx react-native start

# 4. In another terminal, run on iOS
npx react-native run-ios

# 5. Or run on Android
npx react-native run-android
```

### Modifying a Program

1. Open `App.tsx` in your IDE
2. Make changes (e.g., change text, colors, add features)
3. Save the file
4. Press 'R' twice in Metro terminal for reload
5. Or enable Hot Reloading (Cmd/Ctrl + D → Enable Hot Reloading)

---

## 🔍 Code Quality

### Best Practices Implemented

✅ **TypeScript Conventions**
- Type annotations for props and state
- Interface definitions
- Type-safe components

✅ **React Patterns**
- Functional components
- React Hooks
- Proper prop handling
- Component composition

✅ **Code Organization**
- Separation of concerns
- StyleSheet at bottom
- Clear naming conventions
- Consistent structure

✅ **Performance**
- useNativeDriver for animations
- Proper key props
- FlatList for lists
- Memoization where appropriate

---

## 📈 Project Statistics

**Created**: 2025-11-17
**Framework**: React Native
**Language**: TypeScript
**Total Programs**: 100
**Total Code Lines**: ~8,049
**Average Lines/Program**: ~80.5
**Complexity Range**: Beginner to Advanced
**Platform Support**: iOS, Android

---

**Happy React Native Development! 🚀**

For questions or issues, refer to the main repository CLAUDE.md file or consult the official React Native documentation.
