import SwiftUI

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
