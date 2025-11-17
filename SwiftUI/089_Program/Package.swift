// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram089",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram089", targets: ["SwiftUIProgram089"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram089",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
