// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program088",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program088",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
