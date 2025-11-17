// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program013",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program013",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
