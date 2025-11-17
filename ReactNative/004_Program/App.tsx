import React from 'react';
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
