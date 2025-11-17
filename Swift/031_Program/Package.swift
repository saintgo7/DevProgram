// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program031",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program031",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
