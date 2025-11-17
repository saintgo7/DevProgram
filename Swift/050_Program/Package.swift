// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program050",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program050",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
