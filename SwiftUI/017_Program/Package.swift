// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram017",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram017", targets: ["SwiftUIProgram017"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram017",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
