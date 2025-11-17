// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program047",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program047",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
