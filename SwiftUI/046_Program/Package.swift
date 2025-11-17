// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram046",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram046", targets: ["SwiftUIProgram046"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram046",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
