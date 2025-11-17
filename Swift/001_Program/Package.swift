// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program001",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program001",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
