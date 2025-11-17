// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program079",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program079",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
