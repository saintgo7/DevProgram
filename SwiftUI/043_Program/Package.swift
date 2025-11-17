// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram043",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram043", targets: ["SwiftUIProgram043"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram043",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
