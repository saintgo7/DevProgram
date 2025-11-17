// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram039",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram039", targets: ["SwiftUIProgram039"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram039",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
