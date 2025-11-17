// Text Statistics
using System;
using System.IO;
using System.Linq;
class Program { static void Main() { Console.Write("File: "); var text = File.ReadAllText(Console.ReadLine()); Console.WriteLine($"Characters: {text.Length}"); Console.WriteLine($"Words: {text.Split(' ', StringSplitOptions.RemoveEmptyEntries).Length}"); Console.WriteLine($"Lines: {text.Split('\n').Length}"); } }