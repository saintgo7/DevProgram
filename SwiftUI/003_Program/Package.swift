// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram003",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram003", targets: ["SwiftUIProgram003"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram003",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
