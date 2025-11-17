// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram007",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram007", targets: ["SwiftUIProgram007"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram007",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
