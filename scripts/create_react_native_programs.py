#!/usr/bin/env python3
"""
Create 100 React Native programs
"""

import os
import json

base_dir = "/home/user/DevProgram/ReactNative"

# React Native program templates
react_native_programs = {
    1: ("Hello World App", "Simple React Native hello world", """import React from 'react';
import {SafeAreaView, View, Text, StyleSheet} from 'react-native';

const App = () => {
  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Hello, React Native!</Text>
        <Text style={styles.subtitle}>Welcome to Mobile Development</Text>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginTop: 10,
  },
});

export default App;
"""),

    2: ("Counter App", "Counter with increment/decrement", """import React, {useState} from 'react';
import {SafeAreaView, View, Text, TouchableOpacity, StyleSheet} from 'react-native';

const App = () => {
  const [count, setCount] = useState(0);

  const increment = () => setCount(count + 1);
  const decrement = () => setCount(count - 1);
  const reset = () => setCount(0);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.label}>Counter Value:</Text>
        <Text style={styles.counter}>{count}</Text>
        <View style={styles.buttonRow}>
          <TouchableOpacity style={styles.button} onPress={decrement}>
            <Text style={styles.buttonText}>-</Text>
          </TouchableOpacity>
          <TouchableOpacity style={[styles.button, styles.resetButton]} onPress={reset}>
            <Text style={styles.buttonText}>Reset</Text>
          </TouchableOpacity>
          <TouchableOpacity style={styles.button} onPress={increment}>
            <Text style={styles.buttonText}>+</Text>
          </TouchableOpacity>
        </View>
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  content: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  label: {
    fontSize: 20,
    color: '#666',
  },
  counter: {
    fontSize: 64,
    fontWeight: 'bold',
    color: '#007AFF',
    marginVertical: 20,
  },
  buttonRow: {
    flexDirection: 'row',
    gap: 15,
  },
  button: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 30,
    paddingVertical: 15,
    borderRadius: 8,
    minWidth: 80,
    alignItems: 'center',
  },
  resetButton: {
    backgroundColor: '#FF3B30',
  },
  buttonText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  },
});

export default App;
"""),

    3: ("Text Input App", "Text input and display", """import React, {useState} from 'react';
import {SafeAreaView, View, Text, TextInput, TouchableOpacity, StyleSheet} from 'react-native';

const App = () => {
  const [text, setText] = useState('');
  const [displayText, setDisplayText] = useState('');

  const handleSubmit = () => {
    setDisplayText(text);
    setText('');
  };

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Text Input Demo</Text>
        <TextInput
          style={styles.input}
          placeholder="Enter text here"
          value={text}
          onChangeText={setText}
        />
        <TouchableOpacity style={styles.button} onPress={handleSubmit}>
          <Text style={styles.buttonText}>Submit</Text>
        </TouchableOpacity>
        {displayText ? (
          <View style={styles.resultContainer}>
            <Text style={styles.resultLabel}>You entered:</Text>
            <Text style={styles.resultText}>{displayText}</Text>
          </View>
        ) : null}
      </View>
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  content: {
    flex: 1,
    padding: 20,
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
    textAlign: 'center',
  },
  input: {
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 15,
    fontSize: 16,
    marginBottom: 15,
  },
  button: {
    backgroundColor: '#007AFF',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
  resultContainer: {
    marginTop: 30,
    padding: 20,
    backgroundColor: '#f5f5f5',
    borderRadius: 8,
  },
  resultLabel: {
    fontSize: 16,
    color: '#666',
    marginBottom: 5,
  },
  resultText: {
    fontSize: 20,
    fontWeight: '600',
    color: '#333',
  },
});

export default App;
"""),

    4: ("FlatList App", "Scrollable list with FlatList", """import React from 'react';
import {SafeAreaView, View, Text, FlatList, TouchableOpacity, StyleSheet, Alert} from 'react-native';

const App = () => {
  const data = Array.from({length: 50}, (_, i) => ({
    id: `${i + 1}`,
    title: `Item ${i + 1}`,
    subtitle: `Subtitle for item ${i + 1}`,
  }));

  const renderItem = ({item}) => (
    <TouchableOpacity
      style={styles.item}
      onPress={() => Alert.alert('Item Pressed', `You tapped on ${item.title}`)}>
      <View style={styles.itemContent}>
        <Text style={styles.itemTitle}>{item.title}</Text>
        <Text style={styles.itemSubtitle}>{item.subtitle}</Text>
      </View>
      <Text style={styles.arrow}>›</Text>
    </TouchableOpacity>
  );

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.headerTitle}>FlatList Demo</Text>
      </View>
      <FlatList
        data={data}
        renderItem={renderItem}
        keyExtractor={item => item.id}
        ItemSeparatorComponent={() => <View style={styles.separator} />}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
  },
  header: {
    padding: 20,
    borderBottomWidth: 1,
    borderBottomColor: '#eee',
  },
  headerTitle: {
    fontSize: 24,
    fontWeight: 'bold',
  },
  item: {
    flexDirection: 'row',
    alignItems: 'center',
    padding: 15,
  },
  itemContent: {
    flex: 1,
  },
  itemTitle: {
    fontSize: 16,
    fontWeight: '600',
    color: '#333',
  },
  itemSubtitle: {
    fontSize: 14,
    color: '#666',
    marginTop: 4,
  },
  arrow: {
    fontSize: 24,
    color: '#ccc',
  },
  separator: {
    height: 1,
    backgroundColor: '#eee',
  },
});

export default App;
"""),

    5: ("Todo List App", "Todo list with add/delete", """import React, {useState} from 'react';
import {SafeAreaView, View, Text, TextInput, TouchableOpacity, FlatList, StyleSheet} from 'react-native';

const App = () => {
  const [task, setTask] = useState('');
  const [tasks, setTasks] = useState([]);

  const addTask = () => {
    if (task.trim()) {
      setTasks([...tasks, {id: Date.now().toString(), text: task}]);
      setTask('');
    }
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter(item => item.id !== id));
  };

  const renderTask = ({item}) => (
    <View style={styles.taskItem}>
      <Text style={styles.taskText}>{item.text}</Text>
      <TouchableOpacity onPress={() => deleteTask(item.id)}>
        <Text style={styles.deleteButton}>✕</Text>
      </TouchableOpacity>
    </View>
  );

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Todo List</Text>
      </View>
      <View style={styles.inputContainer}>
        <TextInput
          style={styles.input}
          placeholder="Enter task"
          value={task}
          onChangeText={setTask}
        />
        <TouchableOpacity style={styles.addButton} onPress={addTask}>
          <Text style={styles.addButtonText}>Add</Text>
        </TouchableOpacity>
      </View>
      <FlatList
        data={tasks}
        renderItem={renderTask}
        keyExtractor={item => item.id}
        style={styles.list}
      />
    </SafeAreaView>
  );
};

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#f5f5f5',
  },
  header: {
    padding: 20,
    backgroundColor: '#007AFF',
  },
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    color: '#fff',
  },
  inputContainer: {
    flexDirection: 'row',
    padding: 15,
    backgroundColor: '#fff',
  },
  input: {
    flex: 1,
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 10,
    marginRight: 10,
  },
  addButton: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 20,
    borderRadius: 8,
    justifyContent: 'center',
  },
  addButtonText: {
    color: '#fff',
    fontWeight: '600',
  },
  list: {
    flex: 1,
  },
  taskItem: {
    flexDirection: 'row',
    alignItems: 'center',
    backgroundColor: '#fff',
    padding: 15,
    marginHorizontal: 15,
    marginTop: 10,
    borderRadius: 8,
  },
  taskText: {
    flex: 1,
    fontSize: 16,
  },
  deleteButton: {
    fontSize: 20,
    color: '#FF3B30',
    fontWeight: 'bold',
  },
});

export default App;
"""),
}

# Generate remaining programs
for i in range(6, 101):
    if i <= 20:
        # Basic Components
        template = f"""import React from 'react';
import {{SafeAreaView, View, Text, StyleSheet}} from 'react-native';

const App = () => {{
  return (
    <SafeAreaView style={{styles.container}}>
      <View style={{styles.content}}>
        <Text style={{styles.title}}>React Native App {i:03d}</Text>
        <Text style={{styles.subtitle}}>Basic Components Demo</Text>
      </View>
    </SafeAreaView>
  );
}};

const styles = StyleSheet.create({{
  container: {{
    flex: 1,
    backgroundColor: '#fff',
  }},
  content: {{
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  }},
  title: {{
    fontSize: 24,
    fontWeight: 'bold',
    color: '#333',
  }},
  subtitle: {{
    fontSize: 16,
    color: '#666',
    marginTop: 10,
  }},
}});

export default App;
"""
    elif i <= 40:
        # State Management
        template = f"""import React, {{useState, useEffect}} from 'react';
import {{SafeAreaView, View, Text, TouchableOpacity, StyleSheet}} from 'react-native';

const App = () => {{
  const [isActive, setIsActive] = useState(false);
  const [count, setCount] = useState(0);

  useEffect(() => {{
    console.log('Component mounted');
    return () => console.log('Component unmounted');
  }}, []);

  return (
    <SafeAreaView style={{styles.container}}>
      <View style={{styles.content}}>
        <Text style={{styles.title}}>State Management {i:03d}</Text>
        <Text style={{[styles.status, isActive && styles.activeStatus]}}>
          {{isActive ? 'Active' : 'Inactive'}}
        </Text>
        <Text style={{styles.count}}>Count: {{count}}</Text>
        <TouchableOpacity
          style={{styles.button}}
          onPress={{() => setIsActive(!isActive)}}>
          <Text style={{styles.buttonText}}>Toggle State</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={{[styles.button, styles.countButton]}}
          onPress={{() => setCount(count + 1)}}>
          <Text style={{styles.buttonText}}>Increment</Text>
        </TouchableOpacity>
      </View>
    </SafeAreaView>
  );
}};

const styles = StyleSheet.create({{
  container: {{
    flex: 1,
    backgroundColor: '#f5f5f5',
  }},
  content: {{
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  }},
  title: {{
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  }},
  status: {{
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FF3B30',
    marginVertical: 20,
  }},
  activeStatus: {{
    color: '#34C759',
  }},
  count: {{
    fontSize: 24,
    marginBottom: 20,
  }},
  button: {{
    backgroundColor: '#007AFF',
    paddingHorizontal: 30,
    paddingVertical: 15,
    borderRadius: 8,
    marginTop: 10,
  }},
  countButton: {{
    backgroundColor: '#34C759',
  }},
  buttonText: {{
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  }},
}});

export default App;
"""
    elif i <= 60:
        # Navigation (simplified without navigation library)
        template = f"""import React, {{useState}} from 'react';
import {{SafeAreaView, View, Text, TouchableOpacity, StyleSheet}} from 'react-native';

const FirstScreen = ({{onNavigate}}) => (
  <View style={{styles.screen}}>
    <Text style={{styles.screenTitle}}>First Screen</Text>
    <TouchableOpacity style={{styles.button}} onPress={{onNavigate}}>
      <Text style={{styles.buttonText}}>Go to Second Screen</Text>
    </TouchableOpacity>
  </View>
);

const SecondScreen = ({{onGoBack}}) => (
  <View style={{styles.screen}}>
    <Text style={{styles.screenTitle}}>Second Screen</Text>
    <TouchableOpacity style={{[styles.button, styles.backButton]}} onPress={{onGoBack}}>
      <Text style={{styles.buttonText}}>Go Back</Text>
    </TouchableOpacity>
  </View>
);

const App = () => {{
  const [currentScreen, setCurrentScreen] = useState('first');

  return (
    <SafeAreaView style={{styles.container}}>
      <View style={{styles.header}}>
        <Text style={{styles.title}}>Navigation Demo {i:03d}</Text>
      </View>
      {{currentScreen === 'first' ? (
        <FirstScreen onNavigate={{() => setCurrentScreen('second')}} />
      ) : (
        <SecondScreen onGoBack={{() => setCurrentScreen('first')}} />
      )}}
    </SafeAreaView>
  );
}};

const styles = StyleSheet.create({{
  container: {{
    flex: 1,
    backgroundColor: '#fff',
  }},
  header: {{
    padding: 20,
    backgroundColor: '#007AFF',
  }},
  title: {{
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  }},
  screen: {{
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  }},
  screenTitle: {{
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 30,
  }},
  button: {{
    backgroundColor: '#007AFF',
    paddingHorizontal: 30,
    paddingVertical: 15,
    borderRadius: 8,
  }},
  backButton: {{
    backgroundColor: '#FF3B30',
  }},
  buttonText: {{
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  }},
}});

export default App;
"""
    elif i <= 80:
        # Forms & Input
        template = f"""import React, {{useState}} from 'react';
import {{SafeAreaView, View, Text, TextInput, TouchableOpacity, ScrollView, StyleSheet}} from 'react-native';

const App = () => {{
  const [formData, setFormData] = useState({{
    name: '',
    email: '',
    message: '',
  }});
  const [submitted, setSubmitted] = useState(false);

  const handleSubmit = () => {{
    if (formData.name && formData.email) {{
      setSubmitted(true);
      setTimeout(() => setSubmitted(false), 3000);
    }}
  }};

  return (
    <SafeAreaView style={{styles.container}}>
      <ScrollView style={{styles.scrollView}}>
        <Text style={{styles.title}}>Form Demo {i:03d}</Text>
        <View style={{styles.form}}>
          <Text style={{styles.label}}>Name</Text>
          <TextInput
            style={{styles.input}}
            placeholder="Enter your name"
            value={{formData.name}}
            onChangeText={{text => setFormData({{...formData, name: text}})}}
          />
          <Text style={{styles.label}}>Email</Text>
          <TextInput
            style={{styles.input}}
            placeholder="Enter your email"
            value={{formData.email}}
            onChangeText={{text => setFormData({{...formData, email: text}})}}
            keyboardType="email-address"
          />
          <Text style={{styles.label}}>Message</Text>
          <TextInput
            style={{[styles.input, styles.textArea]}}
            placeholder="Enter your message"
            value={{formData.message}}
            onChangeText={{text => setFormData({{...formData, message: text}})}}
            multiline
            numberOfLines={{4}}
          />
          <TouchableOpacity style={{styles.button}} onPress={{handleSubmit}}>
            <Text style={{styles.buttonText}}>Submit</Text>
          </TouchableOpacity>
          {{submitted && (
            <View style={{styles.successMessage}}>
              <Text style={{styles.successText}}>Form submitted successfully!</Text>
            </View>
          )}}
        </View>
      </ScrollView>
    </SafeAreaView>
  );
}};

const styles = StyleSheet.create({{
  container: {{
    flex: 1,
    backgroundColor: '#f5f5f5',
  }},
  scrollView: {{
    flex: 1,
  }},
  title: {{
    fontSize: 24,
    fontWeight: 'bold',
    padding: 20,
    backgroundColor: '#007AFF',
    color: '#fff',
  }},
  form: {{
    padding: 20,
  }},
  label: {{
    fontSize: 16,
    fontWeight: '600',
    marginTop: 15,
    marginBottom: 5,
  }},
  input: {{
    borderWidth: 1,
    borderColor: '#ddd',
    borderRadius: 8,
    padding: 12,
    fontSize: 16,
    backgroundColor: '#fff',
  }},
  textArea: {{
    height: 100,
    textAlignVertical: 'top',
  }},
  button: {{
    backgroundColor: '#007AFF',
    padding: 15,
    borderRadius: 8,
    alignItems: 'center',
    marginTop: 20,
  }},
  buttonText: {{
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  }},
  successMessage: {{
    backgroundColor: '#34C759',
    padding: 15,
    borderRadius: 8,
    marginTop: 15,
  }},
  successText: {{
    color: '#fff',
    textAlign: 'center',
    fontWeight: '600',
  }},
}});

export default App;
"""
    else:
        # Advanced Features
        template = f"""import React, {{useState, useEffect}} from 'react';
import {{SafeAreaView, View, Text, Animated, StyleSheet}} from 'react-native';

const App = () => {{
  const [fadeAnim] = useState(new Animated.Value(0));

  useEffect(() => {{
    Animated.loop(
      Animated.sequence([
        Animated.timing(fadeAnim, {{
          toValue: 1,
          duration: 1000,
          useNativeDriver: true,
        }}),
        Animated.timing(fadeAnim, {{
          toValue: 0,
          duration: 1000,
          useNativeDriver: true,
        }}),
      ])
    ).start();
  }}, [fadeAnim]);

  return (
    <SafeAreaView style={{styles.container}}>
      <View style={{styles.content}}>
        <Text style={{styles.title}}>Advanced Features {i:03d}</Text>
        <Text style={{styles.subtitle}}>Animation Demo</Text>
        <Animated.View style={{[styles.animatedBox, {{opacity: fadeAnim}}]}}>
          <Text style={{styles.animatedText}}>Fading Animation</Text>
        </Animated.View>
      </View>
    </SafeAreaView>
  );
}};

const styles = StyleSheet.create({{
  container: {{
    flex: 1,
    backgroundColor: '#fff',
  }},
  content: {{
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  }},
  title: {{
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 10,
  }},
  subtitle: {{
    fontSize: 16,
    color: '#666',
    marginBottom: 30,
  }},
  animatedBox: {{
    width: 150,
    height: 150,
    backgroundColor: '#007AFF',
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
  }},
  animatedText: {{
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  }},
}});

export default App;
"""

    react_native_programs[i] = (f"Program {i}", f"React Native program {i}", template)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in react_native_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write App.tsx
    with open(f"{program_dir}/App.tsx", 'w') as f:
        f.write(code)

    # Create package.json
    package_json = {
        "name": f"react-native-program-{num:03d}",
        "version": "1.0.0",
        "description": desc,
        "main": "index.js",
        "scripts": {
            "android": "react-native run-android",
            "ios": "react-native run-ios",
            "start": "react-native start",
            "test": "jest"
        },
        "dependencies": {
            "react": "18.2.0",
            "react-native": "0.72.0"
        },
        "devDependencies": {
            "@babel/core": "^7.20.0",
            "@babel/preset-env": "^7.20.0",
            "@babel/runtime": "^7.20.0",
            "@react-native/eslint-config": "^0.72.0",
            "@react-native/metro-config": "^0.72.0",
            "@tsconfig/react-native": "^3.0.0",
            "@types/react": "^18.0.24",
            "@types/react-test-renderer": "^18.0.0",
            "babel-jest": "^29.2.1",
            "eslint": "^8.19.0",
            "jest": "^29.2.1",
            "metro-react-native-babel-preset": "0.76.0",
            "prettier": "^2.4.1",
            "react-test-renderer": "18.2.0",
            "typescript": "4.8.4"
        },
        "engines": {
            "node": ">=16"
        }
    }

    with open(f"{program_dir}/package.json", 'w') as f:
        json.dump(package_json, f, indent=2)

    # Create tsconfig.json
    tsconfig = {
        "extends": "@tsconfig/react-native/tsconfig.json",
        "compilerOptions": {
            "strict": True,
            "esModuleInterop": True,
            "skipLibCheck": True
        }
    }

    with open(f"{program_dir}/tsconfig.json", 'w') as f:
        json.dump(tsconfig, f, indent=2)

    print(f"Created: {num:03d} - {title}")

print(f"\nCreated {len(react_native_programs)} React Native programs in {base_dir}")
