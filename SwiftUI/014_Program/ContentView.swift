import SwiftUI

struct ContentView: View {
    @State private var isActive = false

    var body: some View {
        VStack(spacing: 20) {
            Text("SwiftUI Program 014")
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("Basic SwiftUI View")
                .font(.headline)
                .foregroundColor(.gray)

            Button(action: { isActive.toggle() }) {
                Text(isActive ? "Active" : "Inactive")
                    .padding()
                    .background(isActive ? Color.green : Color.gray)
                    .foregroundColor(.white)
                    .cornerRadius(10)
            }
        }
        .padding()
    }
}

@main
struct Program014App: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
