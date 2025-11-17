// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram061",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram061", targets: ["SwiftUIProgram061"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram061",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
