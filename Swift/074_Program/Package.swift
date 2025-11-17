// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program074",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program074",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
