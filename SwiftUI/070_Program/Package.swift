// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram070",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram070", targets: ["SwiftUIProgram070"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram070",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
