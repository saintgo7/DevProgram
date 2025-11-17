// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program076",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program076",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
