// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program053",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program053",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
