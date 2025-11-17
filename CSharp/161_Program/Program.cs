// Async File Reader
using System;
using System.IO;
using System.Threading.Tasks;
class Program { static async Task Main() { Console.Write("File: "); var content = await File.ReadAllTextAsync(Console.ReadLine()); Console.WriteLine(content); } }