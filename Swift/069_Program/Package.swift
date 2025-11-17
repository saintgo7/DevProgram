// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program069",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program069",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
