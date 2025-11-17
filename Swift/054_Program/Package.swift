// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program054",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program054",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
