// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram031",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram031", targets: ["SwiftUIProgram031"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram031",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
