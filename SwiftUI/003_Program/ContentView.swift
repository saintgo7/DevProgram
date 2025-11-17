import SwiftUI

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
                    ForEach(tasks.indices, id: \.self) { index in
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
