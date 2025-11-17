var builder = WebApplication.CreateBuilder(args);
var app = builder.Build();

app.MapGet("/", () => "File Upload");

app.Run();
