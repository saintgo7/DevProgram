// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program035",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program035",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
