// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram015",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram015", targets: ["SwiftUIProgram015"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram015",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
