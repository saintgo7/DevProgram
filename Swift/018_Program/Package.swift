// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program018",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program018",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
