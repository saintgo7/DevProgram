// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program034",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program034",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
