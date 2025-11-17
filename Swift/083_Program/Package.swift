// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program083",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program083",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
