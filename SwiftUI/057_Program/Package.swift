// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram057",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram057", targets: ["SwiftUIProgram057"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram057",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
