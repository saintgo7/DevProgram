// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program072",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program072",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
