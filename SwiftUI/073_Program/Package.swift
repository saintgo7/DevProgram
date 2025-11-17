// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram073",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram073", targets: ["SwiftUIProgram073"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram073",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
