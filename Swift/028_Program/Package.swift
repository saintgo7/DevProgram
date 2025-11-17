// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program028",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program028",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
