// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program060",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program060",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
