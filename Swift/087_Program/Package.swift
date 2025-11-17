// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program087",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program087",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
