// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program064",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program064",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
