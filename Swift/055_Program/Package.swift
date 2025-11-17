// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program055",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program055",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
