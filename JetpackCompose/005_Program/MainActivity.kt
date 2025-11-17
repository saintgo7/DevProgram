package com.example.program005

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.clickable
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import androidx.navigation.compose.rememberNavController

data class Item(val id: Int, val title: String, val subtitle: String)

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                NavigationApp()
            }
        }
    }
}

@Composable
fun NavigationApp() {
    val navController = rememberNavController()
    val items = remember {
        List(10) { Item(it, "Item ${it + 1}", "Subtitle ${it + 1}") }
    }

    NavHost(navController, startDestination = "list") {
        composable("list") {
            ListScreen(items) { item ->
                navController.navigate("detail/${item.id}")
            }
        }
        composable("detail/{itemId}") { backStackEntry ->
            val itemId = backStackEntry.arguments?.getString("itemId")?.toInt()
            val item = items.find { it.id == itemId }
            if (item != null) {
                DetailScreen(item) {
                    navController.popBackStack()
                }
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ListScreen(items: List<Item>, onItemClick: (Item) -> Unit) {
    Scaffold(
        topBar = { TopAppBar(title = { Text("Items") }) }
    ) { paddingValues ->
        LazyColumn(
            modifier = Modifier.padding(paddingValues),
            contentPadding = PaddingValues(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {
            items(items) { item ->
                Card(
                    modifier = Modifier
                        .fillMaxWidth()
                        .clickable { onItemClick(item) }
                ) {
                    Column(modifier = Modifier.padding(16.dp)) {
                        Text(item.title, style = MaterialTheme.typography.titleMedium)
                        Text(item.subtitle, style = MaterialTheme.typography.bodyMedium)
                    }
                }
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun DetailScreen(item: Item, onBack: () -> Unit) {
    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Details") },
                navigationIcon = {
                    IconButton(onClick = onBack) {
                        Icon(Icons.Default.ArrowBack, "Back")
                    }
                }
            )
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .padding(paddingValues)
                .padding(16.dp)
        ) {
            Text(item.title, style = MaterialTheme.typography.headlineLarge)
            Spacer(modifier = Modifier.height(16.dp))
            Text(item.subtitle, style = MaterialTheme.typography.bodyLarge)
        }
    }
}
