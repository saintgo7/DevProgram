// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram059",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram059", targets: ["SwiftUIProgram059"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram059",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
