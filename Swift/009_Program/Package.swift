// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program009",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program009",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
