// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program012",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program012",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
