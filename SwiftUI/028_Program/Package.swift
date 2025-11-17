// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram028",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram028", targets: ["SwiftUIProgram028"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram028",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
