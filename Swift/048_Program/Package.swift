// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program048",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program048",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
