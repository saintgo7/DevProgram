// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program063",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program063",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
