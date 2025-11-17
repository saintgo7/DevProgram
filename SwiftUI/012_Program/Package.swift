// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram012",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram012", targets: ["SwiftUIProgram012"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram012",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
