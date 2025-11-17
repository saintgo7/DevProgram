// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram064",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram064", targets: ["SwiftUIProgram064"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram064",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
