// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program098",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program098",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
