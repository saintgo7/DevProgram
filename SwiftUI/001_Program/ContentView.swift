import SwiftUI

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
