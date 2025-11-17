// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram014",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram014", targets: ["SwiftUIProgram014"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram014",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
