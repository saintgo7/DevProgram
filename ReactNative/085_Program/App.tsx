import React, {useState, useEffect} from 'react';
import {SafeAreaView, View, Text, Animated, StyleSheet} from 'react-native';

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
  }, [fadeAnim]);

  return (
    <SafeAreaView style={styles.container}>
      <View style={styles.content}>
        <Text style={styles.title}>Advanced Features 085</Text>
        <Text style={styles.subtitle}>Animation Demo</Text>
        <Animated.View style={[styles.animatedBox, {opacity: fadeAnim}]}>
          <Text style={styles.animatedText}>Fading Animation</Text>
        </Animated.View>
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
    marginBottom: 10,
  },
  subtitle: {
    fontSize: 16,
    color: '#666',
    marginBottom: 30,
  },
  animatedBox: {
    width: 150,
    height: 150,
    backgroundColor: '#007AFF',
    borderRadius: 20,
    justifyContent: 'center',
    alignItems: 'center',
  },
  animatedText: {
    color: '#fff',
    fontSize: 18,
    fontWeight: '600',
  },
});

export default App;
