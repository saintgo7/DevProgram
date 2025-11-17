// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program025",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program025",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
