// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram022",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram022", targets: ["SwiftUIProgram022"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram022",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
