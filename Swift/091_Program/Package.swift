// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program091",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program091",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
