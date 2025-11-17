// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram072",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram072", targets: ["SwiftUIProgram072"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram072",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
