// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram083",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram083", targets: ["SwiftUIProgram083"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram083",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
