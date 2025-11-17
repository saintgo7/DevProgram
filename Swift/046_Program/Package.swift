// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program046",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program046",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
