// JSON Writer
using System;
using System.Text.Json;
class Program { static void Main() { var person = new { Name = "John", Age = 30 }; var json = JsonSerializer.Serialize(person); Console.WriteLine(json); } }