// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program100",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program100",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
