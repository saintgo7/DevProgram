// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram076",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram076", targets: ["SwiftUIProgram076"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram076",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
