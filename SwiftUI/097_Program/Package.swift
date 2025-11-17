// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram097",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram097", targets: ["SwiftUIProgram097"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram097",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
