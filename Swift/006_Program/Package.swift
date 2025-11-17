// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program006",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program006",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
