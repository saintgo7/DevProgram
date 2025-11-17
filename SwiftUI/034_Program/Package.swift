// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram034",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram034", targets: ["SwiftUIProgram034"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram034",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
