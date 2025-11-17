# ASP.NET Core Programs

100 ASP.NET Core programs demonstrating C# web framework.

## Features
- Cross-platform (.NET 8)
- MVC Pattern
- Razor Pages
- Web API
- Entity Framework Core
- Dependency Injection
- Middleware Pipeline
- SignalR for Real-time

## Prerequisites

- .NET 8 SDK or later
- Visual Studio Code or Visual Studio

## Quick Start

```bash
cd ASP.NET/001_HelloWorld
dotnet restore
dotnet run
# Visit http://localhost:5000
```

## Build for Production

```bash
dotnet build -c Release
dotnet publish -c Release -o ./publish
```

## Entity Framework Migrations

```bash
dotnet ef migrations add InitialCreate
dotnet ef database update
```

## Watch Mode (Auto-reload)

```bash
dotnet watch run
```
