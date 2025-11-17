// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram093",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram093", targets: ["SwiftUIProgram093"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram093",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
