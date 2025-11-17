// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram020",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram020", targets: ["SwiftUIProgram020"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram020",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
