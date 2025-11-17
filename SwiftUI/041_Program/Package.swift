// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram041",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram041", targets: ["SwiftUIProgram041"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram041",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
