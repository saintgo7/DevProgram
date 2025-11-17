// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program078",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program078",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
