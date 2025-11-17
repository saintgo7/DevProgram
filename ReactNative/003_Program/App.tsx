import React, {useState} from 'react';
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
