// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram092",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram092", targets: ["SwiftUIProgram092"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram092",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
