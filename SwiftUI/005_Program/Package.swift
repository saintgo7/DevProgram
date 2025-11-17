// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram005",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram005", targets: ["SwiftUIProgram005"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram005",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
