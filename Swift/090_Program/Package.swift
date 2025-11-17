// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program090",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program090",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
