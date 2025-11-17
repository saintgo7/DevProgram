// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program042",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program042",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
