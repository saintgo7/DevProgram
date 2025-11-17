// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program016",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program016",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
