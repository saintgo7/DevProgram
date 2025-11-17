// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram060",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram060", targets: ["SwiftUIProgram060"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram060",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
