// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram091",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram091", targets: ["SwiftUIProgram091"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram091",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
