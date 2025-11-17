// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram078",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram078", targets: ["SwiftUIProgram078"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram078",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
