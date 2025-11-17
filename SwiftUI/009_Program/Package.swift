// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram009",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram009", targets: ["SwiftUIProgram009"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram009",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
