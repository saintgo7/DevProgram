// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program033",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program033",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
