// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program014",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program014",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
