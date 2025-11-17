// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram071",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram071", targets: ["SwiftUIProgram071"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram071",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
