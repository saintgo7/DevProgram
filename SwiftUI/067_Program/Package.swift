// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram067",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram067", targets: ["SwiftUIProgram067"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram067",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
