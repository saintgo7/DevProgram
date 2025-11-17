// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program099",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program099",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
