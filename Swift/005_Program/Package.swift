// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program005",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program005",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
