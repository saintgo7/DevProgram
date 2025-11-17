// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram054",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram054", targets: ["SwiftUIProgram054"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram054",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
