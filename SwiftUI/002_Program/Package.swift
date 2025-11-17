// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram002",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram002", targets: ["SwiftUIProgram002"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram002",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
