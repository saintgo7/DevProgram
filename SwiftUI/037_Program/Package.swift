// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram037",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram037", targets: ["SwiftUIProgram037"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram037",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
