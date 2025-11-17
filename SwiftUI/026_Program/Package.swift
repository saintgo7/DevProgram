// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram026",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram026", targets: ["SwiftUIProgram026"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram026",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
