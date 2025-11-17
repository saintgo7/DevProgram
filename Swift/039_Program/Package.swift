// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program039",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program039",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
