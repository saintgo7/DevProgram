// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program094",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program094",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
