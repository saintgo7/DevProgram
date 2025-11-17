// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram088",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram088", targets: ["SwiftUIProgram088"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram088",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
