// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram075",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram075", targets: ["SwiftUIProgram075"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram075",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
