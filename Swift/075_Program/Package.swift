// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program075",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program075",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
