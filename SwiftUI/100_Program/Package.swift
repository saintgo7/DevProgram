// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram100",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram100", targets: ["SwiftUIProgram100"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram100",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
