// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram049",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram049", targets: ["SwiftUIProgram049"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram049",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
