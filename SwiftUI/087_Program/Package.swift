// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram087",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram087", targets: ["SwiftUIProgram087"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram087",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
