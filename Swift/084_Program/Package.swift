// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program084",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program084",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
