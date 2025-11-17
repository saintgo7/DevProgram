// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program011",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program011",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
