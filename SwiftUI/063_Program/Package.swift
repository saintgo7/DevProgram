// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram063",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram063", targets: ["SwiftUIProgram063"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram063",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
