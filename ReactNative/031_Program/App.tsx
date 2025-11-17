import React, {useState, useEffect} from 'react';
import {SafeAreaView, View, Text, TouchableOpacity, StyleSheet} from 'react-native';

const App = () => {
  const [isActive, setIsActive] = useState(false);
  const [count, setCount] = useState(0);

  useEffect(() => {
    console.log('Component mounted');
    return () => console.log('Component unmounted');
  }, []);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>State Management 031</Text>
        <Text style={[styles.status, isActive && styles.activeStatus]}>
          {isActive ? 'Active' : 'Inactive'}
        </Text>
        <Text style={styles.count}>Count: {count}</Text>
        <TouchableOpacity
          style={styles.button}
          onPress={() => setIsActive(!isActive)}>
          <Text style={styles.buttonText}>Toggle State</Text>
        </TouchableOpacity>
        <TouchableOpacity
          style={[styles.button, styles.countButton]}
          onPress={() => setCount(count + 1)}>
          <Text style={styles.buttonText}>Increment</Text>
        </TouchableOpacity>
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
  title: {
    fontSize: 24,
    fontWeight: 'bold',
    marginBottom: 20,
  },
  status: {
    fontSize: 32,
    fontWeight: 'bold',
    color: '#FF3B30',
    marginVertical: 20,
  },
  activeStatus: {
    color: '#34C759',
  },
  count: {
    fontSize: 24,
    marginBottom: 20,
  },
  button: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 30,
    paddingVertical: 15,
    borderRadius: 8,
    marginTop: 10,
  },
  countButton: {
    backgroundColor: '#34C759',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});

export default App;
