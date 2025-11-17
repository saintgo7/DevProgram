// Connection String Builder
using System;
class Program { static void Main() { Console.Write("Server: "); var server = Console.ReadLine(); Console.Write("Database: "); var db = Console.ReadLine(); var connStr = $"Server={server};Database={db};Integrated Security=true;"; Console.WriteLine($"\nConnection String:\n{connStr}"); } }