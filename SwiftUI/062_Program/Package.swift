// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram062",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram062", targets: ["SwiftUIProgram062"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram062",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
