// JSON Reader
using System;
using System.Text.Json;
class Program { static void Main() { var json = "{\"name\":\"John\",\"age\":30}"; var doc = JsonDocument.Parse(json); Console.WriteLine($"Name: {doc.RootElement.GetProperty("name")}"); } }