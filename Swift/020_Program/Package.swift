// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program020",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program020",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
