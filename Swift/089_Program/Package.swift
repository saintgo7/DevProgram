// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program089",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program089",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
