// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program036",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program036",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
