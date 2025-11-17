// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram081",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram081", targets: ["SwiftUIProgram081"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram081",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
