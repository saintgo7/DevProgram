// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram099",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram099", targets: ["SwiftUIProgram099"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram099",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
