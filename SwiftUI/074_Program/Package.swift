// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram074",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram074", targets: ["SwiftUIProgram074"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram074",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
