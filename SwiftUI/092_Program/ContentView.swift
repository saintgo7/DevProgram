import SwiftUI

struct ContentView: View {
    @State private var isAnimating = false
    @State private var scale: CGFloat = 1.0

    var body: some View {
        VStack(spacing: 30) {
            Text("Advanced 092")
                .font(.largeTitle)

            Circle()
                .fill(Color.blue)
                .frame(width: 100, height: 100)
                .scaleEffect(scale)
                .animation(.easeInOut(duration: 1).repeatForever(autoreverses: true), value: scale)

            Button("Animate") {
                scale = scale == 1.0 ? 1.5 : 1.0
            }
            .buttonStyle(.borderedProminent)
        }
        .padding()
        .onAppear {
            scale = 1.5
        }
    }
}

@main
struct AdvancedApp092: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
