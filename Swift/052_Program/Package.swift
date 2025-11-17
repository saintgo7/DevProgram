// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program052",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program052",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
