// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram018",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram018", targets: ["SwiftUIProgram018"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram018",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
