// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program021",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program021",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
