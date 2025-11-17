// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram040",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram040", targets: ["SwiftUIProgram040"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram040",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
