// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program029",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program029",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
