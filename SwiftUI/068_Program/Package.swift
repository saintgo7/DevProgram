// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram068",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram068", targets: ["SwiftUIProgram068"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram068",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
