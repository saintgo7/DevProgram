// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram098",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram098", targets: ["SwiftUIProgram098"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram098",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
