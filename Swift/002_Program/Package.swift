// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program002",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program002",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
