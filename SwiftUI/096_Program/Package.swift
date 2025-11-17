// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram096",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram096", targets: ["SwiftUIProgram096"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram096",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
