// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program032",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program032",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
