// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program086",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program086",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
