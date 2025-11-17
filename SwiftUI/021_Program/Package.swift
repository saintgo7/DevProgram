// swift-tools-version:5.9
import PackageDescription

let package = Package(
    name: "SwiftUIProgram021",
    platforms: [
        .iOS(.v17),
        .macOS(.v14)
    ],
    products: [
        .executable(name: "SwiftUIProgram021", targets: ["SwiftUIProgram021"])
    ],
    targets: [
        .executableTarget(
            name: "SwiftUIProgram021",
            path: ".",
            sources: ["ContentView.swift"]
        )
    ]
)
