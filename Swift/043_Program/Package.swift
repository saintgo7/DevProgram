// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program043",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program043",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
