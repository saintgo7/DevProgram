// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram025",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram025", targets: ["SwiftUIProgram025"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram025",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
