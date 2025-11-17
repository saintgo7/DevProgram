// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program007",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program007",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
