// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram001",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram001", targets: ["SwiftUIProgram001"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram001",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
