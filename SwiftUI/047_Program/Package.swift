// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram047",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram047", targets: ["SwiftUIProgram047"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram047",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
