var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "JWT Authentication");

app.Run();
