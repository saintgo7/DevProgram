// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program082",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program082",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
