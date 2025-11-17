// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram038",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram038", targets: ["SwiftUIProgram038"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram038",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
