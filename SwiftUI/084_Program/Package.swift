// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram084",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram084", targets: ["SwiftUIProgram084"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram084",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
