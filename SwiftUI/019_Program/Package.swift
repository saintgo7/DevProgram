// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram019",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram019", targets: ["SwiftUIProgram019"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram019",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
