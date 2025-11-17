// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram024",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram024", targets: ["SwiftUIProgram024"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram024",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
