// CSV Reader
using System;
using System.IO;
class Program { static void Main() { Console.Write("CSV file: "); foreach (var line in File.ReadLines(Console.ReadLine())) { var fields = line.Split(','); Console.WriteLine(string.Join(" | ", fields)); } } }