// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram008",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram008", targets: ["SwiftUIProgram008"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram008",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
