var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "Hello ASP.NET Core!");

app.MapGet("/api/hello", () => new { Message = "Hello from ASP.NET Core API!" });

app.MapGet("/api/time", () => new
{
    CurrentTime = DateTime.Now,
    Message = "Server time"
});

app.Run();
