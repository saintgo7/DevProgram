import SwiftUI

struct ContentView: View {
    @State private var text = ""
    @State private var selection = 0
    @State private var sliderValue = 50.0

    var body: some View {
        NavigationView {
            Form {
                Section("Input") {
                    TextField("Enter text", text: $text)
                }

                Section("Picker") {
                    Picker("Selection", selection: $selection) {
                        Text("Option 1").tag(0)
                        Text("Option 2").tag(1)
                        Text("Option 3").tag(2)
                    }
                }

                Section("Slider") {
                    Slider(value: $sliderValue, in: 0...100)
                    Text("Value: \(Int(sliderValue))")
                }
            }
            .navigationTitle("Form 079")
        }
    }
}

@main
struct FormApp079: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
