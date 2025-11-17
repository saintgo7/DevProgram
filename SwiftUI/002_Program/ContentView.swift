import SwiftUI

struct ContentView: View {
    @State private var count = 0

    var body: some View {
        VStack(spacing: 30) {
            Text("Counter App")
                .font(.largeTitle)
                .fontWeight(.bold)

            Text("\(count)")
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
