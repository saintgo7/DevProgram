// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program038",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program038",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
