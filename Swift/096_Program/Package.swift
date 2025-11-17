// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "Program096",
    platforms: [
        .macOS(.v13)
    ],
    targets: [
        .executableTarget(
            name: "Program096",
            path: ".",
            sources: ["main.swift"]
        )
    ]
)
