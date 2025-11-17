// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program041",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program041",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
