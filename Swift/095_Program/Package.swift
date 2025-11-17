// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program095",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program095",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
