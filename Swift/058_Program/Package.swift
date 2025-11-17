// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program058",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program058",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
