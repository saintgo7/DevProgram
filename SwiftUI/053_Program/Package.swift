// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram053",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram053", targets: ["SwiftUIProgram053"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram053",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
