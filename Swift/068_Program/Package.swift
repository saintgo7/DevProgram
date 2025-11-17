// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program068",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program068",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
