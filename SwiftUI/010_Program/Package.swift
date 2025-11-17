// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram010",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram010", targets: ["SwiftUIProgram010"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram010",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
