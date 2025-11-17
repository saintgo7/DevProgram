// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram036",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram036", targets: ["SwiftUIProgram036"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram036",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
