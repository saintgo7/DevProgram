import SwiftUI

struct ContentView: View {
    let items = Array(1...20)

    var body: some View {
        NavigationView {
            List(items, id: \.self) { item in
                HStack {
                    Image(systemName: "star.fill")
                        .foregroundColor(.yellow)
                    Text("Item \(item)")
                        .font(.headline)
                }
            }
            .navigationTitle("List Demo 059")
        }
    }
}

@main
struct ListApp059: App {
    var body: some Scene {
        WindowGroup {
            ContentView()
        }
    }
}

#Preview {
    ContentView()
}
