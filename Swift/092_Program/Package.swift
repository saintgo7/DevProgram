// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program092",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program092",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
