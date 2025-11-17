// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram079",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram079", targets: ["SwiftUIProgram079"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram079",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
