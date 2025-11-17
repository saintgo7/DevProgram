// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program024",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program024",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
