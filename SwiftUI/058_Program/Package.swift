// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram058",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram058", targets: ["SwiftUIProgram058"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram058",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
