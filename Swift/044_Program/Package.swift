// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program044",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program044",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
