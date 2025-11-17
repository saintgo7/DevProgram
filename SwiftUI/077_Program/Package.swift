// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram077",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram077", targets: ["SwiftUIProgram077"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram077",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
