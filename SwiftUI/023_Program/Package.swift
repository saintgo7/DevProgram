// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram023",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram023", targets: ["SwiftUIProgram023"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram023",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
