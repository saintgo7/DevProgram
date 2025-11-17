// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram051",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram051", targets: ["SwiftUIProgram051"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram051",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
