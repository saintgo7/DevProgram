// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram052",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram052", targets: ["SwiftUIProgram052"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram052",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
