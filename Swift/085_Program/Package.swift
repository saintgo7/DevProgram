// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program085",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program085",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
