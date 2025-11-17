// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program040",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program040",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
