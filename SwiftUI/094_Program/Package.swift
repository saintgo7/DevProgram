// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram094",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram094", targets: ["SwiftUIProgram094"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram094",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
