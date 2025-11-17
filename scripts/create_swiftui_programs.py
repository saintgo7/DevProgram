#!/usr/bin/env python3
"""
Create 100 SwiftUI programs
"""

import os

base_dir = "/home/user/DevProgram/SwiftUI"

# SwiftUI program templates
swiftui_programs = {
    1: ("Hello World", "Basic SwiftUI hello world", """import SwiftUI

struct ContentView: View {
    var body: some View {
        VStack(spacing: 20) {
            Text("Hello, SwiftUI!")
                .font(.largeTitle)
                .fontWeight(.bold)
                .foregroundColor(.blue)

            Text("Welcome to SwiftUI Programming")
                .font(.headline)
                .foregroundColor(.gray)
        }
        .padding()
    }
}

@main
struct HelloWorldApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
"""),

    2: ("Counter App", "Counter with increment/decrement", """import SwiftUI

struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack(spacing: 30) {
            Text("Counter App")
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("\\(count)")
                .font(.system(size: 72))
                .fontWeight(.bold)
                .foregroundColor(.blue)

            HStack(spacing: 20) {
                Button(action: { count -= 1 }) {
                    Image(systemName: "minus.circle.fill")
                        .font(.largeTitle)
                }

                Button(action: { count = 0 }) {
                    Text("Reset")
                        .font(.headline)
                        .padding()
                        .background(Color.red)
                        .foregroundColor(.white)
                        .cornerRadius(10)
                }

                Button(action: { count += 1 }) {
                    Image(systemName: "plus.circle.fill")
                        .font(.largeTitle)
                }
            }
        }
        .padding()
    }
}

@main
struct CounterApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
"""),

    3: ("Todo List", "SwiftUI todo list", """import SwiftUI

struct ContentView: View {
    @State private var tasks: [String] = []
    @State private var newTask = ""

    var body: some View {
        NavigationView {
            VStack {
                HStack {
                    TextField("Enter task", text: $newTask)
                        .textFieldStyle(RoundedBorderTextFieldStyle())

                    Button(action: addTask) {
                        Image(systemName: "plus.circle.fill")
                            .font(.title)
                    }
                    .disabled(newTask.isEmpty)
                }
                .padding()

                List {
                    ForEach(tasks.indices, id: \\.self) { index in
                        HStack {
                            Text(tasks[index])
                            Spacer()
                            Button(action: { deleteTask(at: index) }) {
                                Image(systemName: "trash")
                                    .foregroundColor(.red)
                            }
                        }
                    }
                }

                if tasks.isEmpty {
                    Spacer()
                    Text("No tasks yet. Add one above!")
                        .foregroundColor(.gray)
                    Spacer()
                }
            }
            .navigationTitle("Todo List")
        }
    }

    func addTask() {
        if !newTask.isEmpty {
            tasks.append(newTask)
            newTask = ""
        }
    }

    func deleteTask(at index: Int) {
        tasks.remove(at: index)
    }
}

@main
struct TodoApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
"""),

    4: ("Form Input", "SwiftUI form handling", """import SwiftUI

struct ContentView: View {
    @State private var name = ""
    @State private var email = ""
    @State private var message = ""
    @State private var showingAlert = false

    var body: some View {
        NavigationView {
            Form {
                Section(header: Text("Personal Information")) {
                    TextField("Name", text: $name)
                    TextField("Email", text: $email)
                        .keyboardType(.emailAddress)
                        .autocapitalization(.none)
                }

                Section(header: Text("Message")) {
                    TextEditor(text: $message)
                        .frame(height: 100)
                }

                Section {
                    Button("Submit") {
                        showingAlert = true
                    }
                    .disabled(name.isEmpty || email.isEmpty)
                }
            }
            .navigationTitle("Form Demo")
            .alert("Form Submitted", isPresented: $showingAlert) {
                Button("OK", role: .cancel) { }
            } message: {
                Text("Name: \\(name)\\nEmail: \\(email)")
            }
        }
    }
}

@main
struct FormApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
"""),

    5: ("List and Navigation", "SwiftUI navigation example", """import SwiftUI

struct Item: Identifiable {
    let id = UUID()
    let title: String
    let subtitle: String
}

struct DetailView: View {
    let item: Item

    var body: some View {
        VStack(spacing: 20) {
            Text(item.title)
                .font(.largeTitle)
                .fontWeight(.bold)

            Text(item.subtitle)
                .font(.headline)
                .foregroundColor(.gray)

            Spacer()
        }
        .padding()
        .navigationTitle("Details")
    }
}

struct ContentView: View {
    let items = [
        Item(title: "Item 1", subtitle: "Subtitle 1"),
        Item(title: "Item 2", subtitle: "Subtitle 2"),
        Item(title: "Item 3", subtitle: "Subtitle 3"),
        Item(title: "Item 4", subtitle: "Subtitle 4"),
        Item(title: "Item 5", subtitle: "Subtitle 5")
    ]

    var body: some View {
        NavigationView {
            List(items) { item in
                NavigationLink(destination: DetailView(item: item)) {
                    VStack(alignment: .leading) {
                        Text(item.title)
                            .font(.headline)
                        Text(item.subtitle)
                            .font(.subheadline)
                            .foregroundColor(.gray)
                    }
                }
            }
            .navigationTitle("Items")
        }
    }
}

@main
struct NavigationApp: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
"""),
}

# Generate remaining programs (6-100)
for i in range(6, 101):
    if i <= 20:
        # Basic Views
        code = f"""import SwiftUI

struct ContentView: View {{
    @State private var isActive = false

    var body: some View {{
        VStack(spacing: 20) {{
            Text("SwiftUI Program {i:03d}")
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("Basic SwiftUI View")
                .font(.headline)
                .foregroundColor(.gray)

            Button(action: {{ isActive.toggle() }}) {{
                Text(isActive ? "Active" : "Inactive")
                    .padding()
                    .background(isActive ? Color.green : Color.gray)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }}
        }}
        .padding()
    }}
}}

@main
struct Program{i:03d}App: App {{
    var body: some Scene {{
        WindowGroup {{
            ContentView()
        }}
    }}
}}

#Preview {{
    ContentView()
}}
"""
    elif i <= 40:
        # State Management
        code = f"""import SwiftUI

struct ContentView: View {{
    @State private var count = 0
    @State private var isOn = false

    var body: some View {{
        VStack(spacing: 30) {{
            Text("State Demo {i:03d}")
                .font(.largeTitle)

            Text("Count: \\(count)")
                .font(.title)

            Toggle("Switch", isOn: $isOn)
                .padding()

            Text(isOn ? "ON" : "OFF")
                .font(.headline)
                .foregroundColor(isOn ? .green : .red)

            Button("Increment") {{
                count += 1
            }}
            .buttonStyle(.borderedProminent)
        }}
        .padding()
    }}
}}

@main
struct StateApp{i:03d}: App {{
    var body: some Scene {{
        WindowGroup {{
            ContentView()
        }}
    }}
}}

#Preview {{
    ContentView()
}}
"""
    elif i <= 60:
        # Lists and Collections
        code = f"""import SwiftUI

struct ContentView: View {{
    let items = Array(1...20)

    var body: some View {{
        NavigationView {{
            List(items, id: \\.self) {{ item in
                HStack {{
                    Image(systemName: "star.fill")
                        .foregroundColor(.yellow)
                    Text("Item \\(item)")
                        .font(.headline)
                }}
            }}
            .navigationTitle("List Demo {i:03d}")
        }}
    }}
}}

@main
struct ListApp{i:03d}: App {{
    var body: some Scene {{
        WindowGroup {{
            ContentView()
        }}
    }}
}}

#Preview {{
    ContentView()
}}
"""
    elif i <= 80:
        # Forms and Controls
        code = f"""import SwiftUI

struct ContentView: View {{
    @State private var text = ""
    @State private var selection = 0
    @State private var sliderValue = 50.0

    var body: some View {{
        NavigationView {{
            Form {{
                Section("Input") {{
                    TextField("Enter text", text: $text)
                }}

                Section("Picker") {{
                    Picker("Selection", selection: $selection) {{
                        Text("Option 1").tag(0)
                        Text("Option 2").tag(1)
                        Text("Option 3").tag(2)
                    }}
                }}

                Section("Slider") {{
                    Slider(value: $sliderValue, in: 0...100)
                    Text("Value: \\(Int(sliderValue))")
                }}
            }}
            .navigationTitle("Form {i:03d}")
        }}
    }}
}}

@main
struct FormApp{i:03d}: App {{
    var body: some Scene {{
        WindowGroup {{
            ContentView()
        }}
    }}
}}

#Preview {{
    ContentView()
}}
"""
    else:
        # Advanced Features
        code = f"""import SwiftUI

struct ContentView: View {{
    @State private var isAnimating = false
    @State private var scale: CGFloat = 1.0

    var body: some View {{
        VStack(spacing: 30) {{
            Text("Advanced {i:03d}")
                .font(.largeTitle)

            Circle()
                .fill(Color.blue)
                .frame(width: 100, height: 100)
                .scaleEffect(scale)
                .animation(.easeInOut(duration: 1).repeatForever(autoreverses: true), value: scale)

            Button("Animate") {{
                scale = scale == 1.0 ? 1.5 : 1.0
            }}
            .buttonStyle(.borderedProminent)
        }}
        .padding()
        .onAppear {{
            scale = 1.5
        }}
    }}
}}

@main
struct AdvancedApp{i:03d}: App {{
    var body: some Scene {{
        WindowGroup {{
            ContentView()
        }}
    }}
}}

#Preview {{
    ContentView()
}}
"""

    swiftui_programs[i] = (f"Program {i}", f"SwiftUI program {i}", code)

# Create directories and files
os.makedirs(base_dir, exist_ok=True)

for num, (title, desc, code) in swiftui_programs.items():
    program_dir = f"{base_dir}/{num:03d}_Program"
    os.makedirs(program_dir, exist_ok=True)

    # Write ContentView.swift
    with open(f"{program_dir}/ContentView.swift", 'w') as f:
        f.write(code)

    # Create Package.swift
    package_swift = f"""// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram{num:03d}",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram{num:03d}", targets: ["SwiftUIProgram{num:03d}"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram{num:03d}",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
"""

    with open(f"{program_dir}/Package.swift", 'w') as f:
        f.write(package_swift)

    print(f"Created: {num:03d} - {title}")

print(f"\nCreated {len(swiftui_programs)} SwiftUI programs in {base_dir}")
