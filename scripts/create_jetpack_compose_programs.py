#!/usr/bin/env python3
"""
Create 100 Jetpack Compose programs
"""

import os

base_dir = "/home/user/DevProgram/JetpackCompose"

# Jetpack Compose program templates
compose_programs = {
    1: ("Hello World", "Basic Jetpack Compose hello world", """package com.example.program001

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                HelloWorldScreen()
            }
        }
    }
}

@Composable
fun HelloWorldScreen() {
    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(
            text = "Hello, Jetpack Compose!",
            style = MaterialTheme.typography.headlineLarge
        )
        Spacer(modifier = Modifier.height(16.dp))
        Text(
            text = "Welcome to Modern Android Development",
            style = MaterialTheme.typography.bodyLarge
        )
    }
}
"""),

    2: ("Counter App", "Counter with increment/decrement", """package com.example.program002

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                CounterScreen()
            }
        }
    }
}

@Composable
fun CounterScreen() {
    var count by remember { mutableStateOf(0) }

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {
        Text(
            text = "Counter App",
            style = MaterialTheme.typography.headlineLarge
        )

        Spacer(modifier = Modifier.height(32.dp))

        Text(
            text = "$count",
            style = MaterialTheme.typography.displayLarge
        )

        Spacer(modifier = Modifier.height(32.dp))

        Row(
            horizontalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            Button(onClick = { count-- }) {
                Text("-")
            }

            Button(
                onClick = { count = 0 },
                colors = ButtonDefaults.buttonColors(
                    containerColor = MaterialTheme.colorScheme.error
                )
            ) {
                Text("Reset")
            }

            Button(onClick = { count++ }) {
                Text("+")
            }
        }
    }
}
"""),

    3: ("Todo List", "Jetpack Compose todo list", """package com.example.program003

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.Delete
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                TodoListScreen()
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun TodoListScreen() {
    var tasks by remember { mutableStateOf(listOf<String>()) }
    var newTask by remember { mutableStateOf("") }

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("Todo List") }
            )
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(16.dp)
        ) {
            Row(
                modifier = Modifier.fillMaxWidth(),
                horizontalArrangement = Arrangement.spacedBy(8.dp)
            ) {
                OutlinedTextField(
                    value = newTask,
                    onValueChange = { newTask = it },
                    modifier = Modifier.weight(1f),
                    label = { Text("Enter task") }
                )

                Button(
                    onClick = {
                        if (newTask.isNotBlank()) {
                            tasks = tasks + newTask
                            newTask = ""
                        }
                    }
                ) {
                    Text("Add")
                }
            }

            Spacer(modifier = Modifier.height(16.dp))

            if (tasks.isEmpty()) {
                Text(
                    text = "No tasks yet. Add one above!",
                    modifier = Modifier.align(Alignment.CenterHorizontally),
                    color = MaterialTheme.colorScheme.onSurfaceVariant
                )
            } else {
                LazyColumn(
                    verticalArrangement = Arrangement.spacedBy(8.dp)
                ) {
                    items(tasks) { task ->
                        Card(
                            modifier = Modifier.fillMaxWidth()
                        ) {
                            Row(
                                modifier = Modifier
                                    .fillMaxWidth()
                                    .padding(16.dp),
                                horizontalArrangement = Arrangement.SpaceBetween,
                                verticalAlignment = Alignment.CenterVertically
                            ) {
                                Text(task)
                                IconButton(onClick = { tasks = tasks - task }) {
                                    Icon(Icons.Default.Delete, "Delete")
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
"""),

    4: ("Form Input", "Jetpack Compose form", """package com.example.program004

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        setContent {
            MaterialTheme {
                FormScreen()
            }
        }
    }
}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun FormScreen() {
    var name by remember { mutableStateOf("") }
    var email by remember { mutableStateOf("") }
    var message by remember { mutableStateOf("") }
    var showDialog by remember { mutableStateOf(false) }

    Scaffold(
        topBar = {
            TopAppBar(title = { Text("Form Demo") })
        }
    ) { paddingValues ->
        Column(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {
            OutlinedTextField(
                value = name,
                onValueChange = { name = it },
                label = { Text("Name") },
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = email,
                onValueChange = { email = it },
                label = { Text("Email") },
                modifier = Modifier.fillMaxWidth()
            )

            OutlinedTextField(
                value = message,
                onValueChange = { message = it },
                label = { Text("Message") },
                modifier = Modifier
                    .fillMaxWidth()
                    .height(120.dp),
                maxLines = 5
            )

            Button(
                onClick = { showDialog = true },
                modifier = Modifier.fillMaxWidth(),
                enabled = name.isNotBlank() && email.isNotBlank()
            ) {
                Text("Submit")
            }

            if (showDialog) {
                AlertDialog(
                    onDismissRequest = { showDialog = false },
                    title = { Text("Form Submitted") },
                    text = { Text("Name: $name\\nEmail: $email") },
                    confirmButton = {
                        TextButton(onClick = { showDialog = false }) {
                            Text("OK")
                        }
                    }
                )
            }
        }
    }
}
"""),

    5: ("List and Navigation", "Jetpack Compose navigation", """package com.example.program005

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
"""),
}

# Generate remaining programs (6-100)
for i in range(6, 101):
    if i <= 20:
        # Basic Composables
        code = f"""package com.example.program{i:03d}

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        setContent {{
            MaterialTheme {{
                BasicScreen()
            }}
        }}
    }}
}}

@Composable
fun BasicScreen() {{
    var isActive by remember {{ mutableStateOf(false) }}

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {{
        Text(
            text = "Jetpack Compose Program {i:03d}",
            style = MaterialTheme.typography.headlineLarge
        )

        Spacer(modifier = Modifier.height(16.dp))

        Text(
            text = if (isActive) "Active" else "Inactive",
            style = MaterialTheme.typography.bodyLarge
        )

        Spacer(modifier = Modifier.height(16.dp))

        Button(onClick = {{ isActive = !isActive }}) {{
            Text("Toggle")
        }}
    }}
}}
"""
    elif i <= 40:
        # State Management
        code = f"""package com.example.program{i:03d}

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        setContent {{
            MaterialTheme {{
                StateScreen()
            }}
        }}
    }}
}}

@Composable
fun StateScreen() {{
    var count by remember {{ mutableStateOf(0) }}
    var checked by remember {{ mutableStateOf(false) }}

    Column(
        modifier = Modifier
            .fillMaxSize()
            .padding(16.dp),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {{
        Text(
            text = "State Demo {i:03d}",
            style = MaterialTheme.typography.headlineLarge
        )

        Spacer(modifier = Modifier.height(24.dp))

        Text("Count: $count", style = MaterialTheme.typography.titleLarge)

        Spacer(modifier = Modifier.height(16.dp))

        Row(horizontalArrangement = Arrangement.spacedBy(8.dp)) {{
            Button(onClick = {{ count++ }}) {{
                Text("Increment")
            }}
            Button(onClick = {{ count-- }}) {{
                Text("Decrement")
            }}
        }}

        Spacer(modifier = Modifier.height(24.dp))

        Row(verticalAlignment = Alignment.CenterVertically) {{
            Checkbox(checked = checked, onCheckedChange = {{ checked = it }})
            Text("Checked: $checked")
        }}
    }}
}}
"""
    elif i <= 60:
        # Lists and LazyColumn
        code = f"""package com.example.program{i:03d}

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.foundation.lazy.items
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        setContent {{
            MaterialTheme {{
                ListScreen()
            }}
        }}
    }}
}}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun ListScreen() {{
    val items = remember {{ List(30) {{ "Item ${{it + 1}}" }} }}

    Scaffold(
        topBar = {{
            TopAppBar(title = {{ Text("List Demo {i:03d}") }})
        }}
    ) {{ paddingValues ->
        LazyColumn(
            modifier = Modifier.padding(paddingValues),
            contentPadding = PaddingValues(16.dp),
            verticalArrangement = Arrangement.spacedBy(8.dp)
        ) {{
            items(items) {{ item ->
                Card(modifier = Modifier.fillMaxWidth()) {{
                    Text(
                        text = item,
                        modifier = Modifier.padding(16.dp),
                        style = MaterialTheme.typography.bodyLarge
                    )
                }}
            }}
        }}
    }}
}}
"""
    elif i <= 80:
        # Forms and Input
        code = f"""package com.example.program{i:03d}

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.foundation.layout.*
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        setContent {{
            MaterialTheme {{
                InputScreen()
            }}
        }}
    }}
}}

@OptIn(ExperimentalMaterial3Api::class)
@Composable
fun InputScreen() {{
    var text by remember {{ mutableStateOf("") }}
    var sliderValue by remember {{ mutableStateOf(50f) }}

    Scaffold(
        topBar = {{
            TopAppBar(title = {{ Text("Input Demo {i:03d}") }})
        }}
    ) {{ paddingValues ->
        Column(
            modifier = Modifier
                .padding(paddingValues)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(16.dp)
        ) {{
            OutlinedTextField(
                value = text,
                onValueChange = {{ text = it }},
                label = {{ Text("Enter text") }},
                modifier = Modifier.fillMaxWidth()
            )

            Text("Text: $text")

            Slider(
                value = sliderValue,
                onValueChange = {{ sliderValue = it }},
                valueRange = 0f..100f
            )

            Text("Value: ${{sliderValue.toInt()}}")
        }}
    }}
}}
"""
    else:
        # Advanced Features
        code = f"""package com.example.program{i:03d}

import android.os.Bundle
import androidx.activity.ComponentActivity
import androidx.activity.compose.setContent
import androidx.compose.animation.core.*
import androidx.compose.foundation.background
import androidx.compose.foundation.layout.*
import androidx.compose.foundation.shape.CircleShape
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Alignment
import androidx.compose.ui.Modifier
import androidx.compose.ui.draw.scale
import androidx.compose.ui.unit.dp

class MainActivity : ComponentActivity() {{
    override fun onCreate(savedInstanceState: Bundle?) {{
        super.onCreate(savedInstanceState)
        setContent {{
            MaterialTheme {{
                AnimationScreen()
            }}
        }}
    }}
}}

@Composable
fun AnimationScreen() {{
    val infiniteTransition = rememberInfiniteTransition(label = "scale")
    val scale by infiniteTransition.animateFloat(
        initialValue = 1f,
        targetValue = 1.5f,
        animationSpec = infiniteRepeatable(
            animation = tween(1000),
            repeatMode = RepeatMode.Reverse
        ),
        label = "scale"
    )

    Column(
        modifier = Modifier.fillMaxSize(),
        horizontalAlignment = Alignment.CenterHorizontally,
        verticalArrangement = Arrangement.Center
    ) {{
        Text(
            text = "Advanced {i:03d}",
            style = MaterialTheme.typography.headlineLarge
        )

        Spacer(modifier = Modifier.height(32.dp))

        Box(
            modifier = Modifier
                .size(100.dp)
                .scale(scale)
                .background(
                    color = MaterialTheme.colorScheme.primary,
                    shape = CircleShape
                )
        )
    }}
}}
"""

    compose_programs[i] = (f"Program {i}", f"Jetpack Compose program {i}", code)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in compose_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write MainActivity.kt
    with open(f"{program_dir}/MainActivity.kt", 'w') as f:
        f.write(code)

    # Create build.gradle
    build_gradle = f"""plugins {{
    id 'com.android.application'
    id 'org.jetbrains.kotlin.android'
}}

android {{
    namespace 'com.example.program{num:03d}'
    compileSdk 34

    defaultConfig {{
        applicationId "com.example.program{num:03d}"
        minSdk 24
        targetSdk 34
        versionCode 1
        versionName "1.0"
    }}

    buildFeatures {{
        compose true
    }}

    composeOptions {{
        kotlinCompilerExtensionVersion '1.5.3'
    }}

    kotlinOptions {{
        jvmTarget = '1.8'
    }}
}}

dependencies {{
    implementation 'androidx.core:core-ktx:1.12.0'
    implementation 'androidx.activity:activity-compose:1.8.0'
    implementation platform('androidx.compose:compose-bom:2023.10.01')
    implementation 'androidx.compose.ui:ui'
    implementation 'androidx.compose.ui:ui-graphics'
    implementation 'androidx.compose.material3:material3'
    implementation 'androidx.navigation:navigation-compose:2.7.5'
}}
"""

    with open(f"{program_dir}/build.gradle", 'w') as f:
        f.write(build_gradle)

    print(f"Created: {num:03d} - {title}")

print(f"\nCreated {len(compose_programs)} Jetpack Compose programs in {base_dir}")
