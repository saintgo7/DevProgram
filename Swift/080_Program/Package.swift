// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program080",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program080",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
