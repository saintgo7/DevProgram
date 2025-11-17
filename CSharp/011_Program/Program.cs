// Text File Merger
using System;
using System.IO;
using System.Linq;
class Program { static void Main() { Console.Write("Output file: "); var output = Console.ReadLine(); Console.WriteLine("Enter files to merge (one per line, END to finish):"); var files = new System.Collections.Generic.List<string>(); string f; while ((f = Console.ReadLine()) != "END") files.Add(f); File.WriteAllText(output, string.Join("\n", files.SelectMany(File.ReadAllLines))); Console.WriteLine("Merged!"); } }