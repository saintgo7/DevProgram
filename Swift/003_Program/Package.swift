// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program003",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program003",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
