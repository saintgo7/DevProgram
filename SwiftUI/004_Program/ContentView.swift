import SwiftUI

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
                Text("Name: \(name)\nEmail: \(email)")
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
