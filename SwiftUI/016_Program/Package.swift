// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram016",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram016", targets: ["SwiftUIProgram016"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram016",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
