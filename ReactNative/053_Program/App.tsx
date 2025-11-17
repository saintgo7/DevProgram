import React, {useState} from 'react';
import {SafeAreaView, View, Text, TouchableOpacity, StyleSheet} from 'react-native';

const FirstScreen = ({onNavigate}) => (
  <View style={styles.screen}>
    <Text style={styles.screenTitle}>First Screen</Text>
    <TouchableOpacity style={styles.button} onPress={onNavigate}>
      <Text style={styles.buttonText}>Go to Second Screen</Text>
    </TouchableOpacity>
  </View>
);

const SecondScreen = ({onGoBack}) => (
  <View style={styles.screen}>
    <Text style={styles.screenTitle}>Second Screen</Text>
    <TouchableOpacity style={[styles.button, styles.backButton]} onPress={onGoBack}>
      <Text style={styles.buttonText}>Go Back</Text>
    </TouchableOpacity>
  </View>
);

const App = () => {
  const [currentScreen, setCurrentScreen] = useState('first');

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.header}>
        <Text style={styles.title}>Navigation Demo 053</Text>
      </View>
      {currentScreen === 'first' ? (
        <FirstScreen onNavigate={() => setCurrentScreen('second')} />
      ) : (
        <SecondScreen onGoBack={() => setCurrentScreen('first')} />
      )}
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
    backgroundColor: '#007AFF',
  },
  title: {
    fontSize: 20,
    fontWeight: 'bold',
    color: '#fff',
  },
  screen: {
    flex: 1,
    justifyContent: 'center',
    alignItems: 'center',
  },
  screenTitle: {
    fontSize: 28,
    fontWeight: 'bold',
    marginBottom: 30,
  },
  button: {
    backgroundColor: '#007AFF',
    paddingHorizontal: 30,
    paddingVertical: 15,
    borderRadius: 8,
  },
  backButton: {
    backgroundColor: '#FF3B30',
  },
  buttonText: {
    color: '#fff',
    fontSize: 16,
    fontWeight: '600',
  },
});

export default App;
