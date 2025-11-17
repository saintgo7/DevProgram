// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram045",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram045", targets: ["SwiftUIProgram045"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram045",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
