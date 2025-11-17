// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program010",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program010",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
