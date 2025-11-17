// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram048",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram048", targets: ["SwiftUIProgram048"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram048",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
