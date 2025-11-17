// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram066",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram066", targets: ["SwiftUIProgram066"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram066",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
