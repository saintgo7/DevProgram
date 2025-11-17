// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram011",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram011", targets: ["SwiftUIProgram011"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram011",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
