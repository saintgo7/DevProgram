// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program062",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program062",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
