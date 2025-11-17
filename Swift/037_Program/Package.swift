// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program037",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program037",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
