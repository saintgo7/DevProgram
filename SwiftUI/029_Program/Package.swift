// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram029",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram029", targets: ["SwiftUIProgram029"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram029",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
