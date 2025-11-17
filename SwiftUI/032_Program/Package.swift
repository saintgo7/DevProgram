// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram032",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram032", targets: ["SwiftUIProgram032"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram032",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
