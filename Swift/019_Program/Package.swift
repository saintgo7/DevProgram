// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program019",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program019",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
