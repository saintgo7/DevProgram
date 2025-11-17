// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program022",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program022",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
