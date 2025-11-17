// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram013",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram013", targets: ["SwiftUIProgram013"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram013",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
