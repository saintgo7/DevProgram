// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program065",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program065",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
