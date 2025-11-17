// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram080",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram080", targets: ["SwiftUIProgram080"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram080",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
