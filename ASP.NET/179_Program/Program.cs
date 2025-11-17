var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();
app.MapGet("/", () => "ASP.NET Program 179");
app.Run();