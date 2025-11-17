// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram090",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram090", targets: ["SwiftUIProgram090"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram090",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
