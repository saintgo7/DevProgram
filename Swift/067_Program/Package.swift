// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program067",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program067",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
