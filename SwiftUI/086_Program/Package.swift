// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram086",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram086", targets: ["SwiftUIProgram086"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram086",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
