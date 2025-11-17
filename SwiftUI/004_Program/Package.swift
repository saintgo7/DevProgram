// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram004",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram004", targets: ["SwiftUIProgram004"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram004",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
