// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program008",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program008",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
