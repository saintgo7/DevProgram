// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram042",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram042", targets: ["SwiftUIProgram042"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram042",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
