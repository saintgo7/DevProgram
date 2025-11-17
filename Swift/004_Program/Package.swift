// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program004",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program004",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
