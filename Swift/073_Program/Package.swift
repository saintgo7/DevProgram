// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program073",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program073",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
