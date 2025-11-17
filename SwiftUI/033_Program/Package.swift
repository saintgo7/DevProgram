// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram033",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram033", targets: ["SwiftUIProgram033"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram033",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
