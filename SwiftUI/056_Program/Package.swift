// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram056",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram056", targets: ["SwiftUIProgram056"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram056",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
