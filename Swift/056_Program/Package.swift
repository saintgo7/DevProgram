// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program056",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program056",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
