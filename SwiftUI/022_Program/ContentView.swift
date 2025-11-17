import SwiftUI

struct ContentView: View {
    @State private var count = 0
    @State private var isOn = false

    var body: some View {
        VStack(spacing: 30) {
            Text("State Demo 022")
                .font(.largeTitle)

            Text("Count: \(count)")
                .font(.title)

            Toggle("Switch", isOn: $isOn)
                .padding()

            Text(isOn ? "ON" : "OFF")
                .font(.headline)
                .foregroundColor(isOn ? .green : .red)

            Button("Increment") {
                count += 1
            }
            .buttonStyle(.borderedProminent)
        }
        .padding()
    }
}

@main
struct StateApp022: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
