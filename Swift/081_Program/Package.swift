// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program081",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program081",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
