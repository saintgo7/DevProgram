// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program070",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program070",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
