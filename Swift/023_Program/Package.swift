// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program023",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program023",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
