// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram027",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram027", targets: ["SwiftUIProgram027"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram027",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
