// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program061",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program061",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
