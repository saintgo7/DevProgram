// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram095",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram095", targets: ["SwiftUIProgram095"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram095",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
