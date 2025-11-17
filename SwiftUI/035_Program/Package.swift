// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram035",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram035", targets: ["SwiftUIProgram035"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram035",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
