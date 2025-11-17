// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program057",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program057",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
