// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram082",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram082", targets: ["SwiftUIProgram082"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram082",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
