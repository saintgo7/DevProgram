// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program077",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program077",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
