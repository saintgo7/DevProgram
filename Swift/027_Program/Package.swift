// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program027",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program027",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
