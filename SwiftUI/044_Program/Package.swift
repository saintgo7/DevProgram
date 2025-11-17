// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram044",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram044", targets: ["SwiftUIProgram044"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram044",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
