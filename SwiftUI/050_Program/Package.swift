// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram050",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram050", targets: ["SwiftUIProgram050"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram050",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
