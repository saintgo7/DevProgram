// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram085",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram085", targets: ["SwiftUIProgram085"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram085",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
