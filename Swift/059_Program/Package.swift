// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program059",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program059",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
