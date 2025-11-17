// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program066",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program066",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
