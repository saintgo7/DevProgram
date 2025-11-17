// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram055",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram055", targets: ["SwiftUIProgram055"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram055",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
