// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram006",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram006", targets: ["SwiftUIProgram006"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram006",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
