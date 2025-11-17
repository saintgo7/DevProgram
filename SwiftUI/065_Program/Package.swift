// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram065",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram065", targets: ["SwiftUIProgram065"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram065",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
