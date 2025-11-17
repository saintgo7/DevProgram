// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram069",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram069", targets: ["SwiftUIProgram069"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram069",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
