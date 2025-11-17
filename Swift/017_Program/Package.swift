// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program017",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program017",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
