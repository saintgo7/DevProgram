// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram030",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram030", targets: ["SwiftUIProgram030"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram030",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
