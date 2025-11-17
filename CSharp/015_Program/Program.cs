// Duplicate Finder
using System;
using System.IO;
using System.Linq;
class Program { static void Main() { Console.Write("Directory: "); var files = Directory.GetFiles(Console.ReadLine()); var duplicates = files.GroupBy(f => new FileInfo(f).Length).Where(g => g.Count() > 1); foreach (var g in duplicates) { Console.WriteLine($"\nSize {g.Key}:"); foreach (var f in g) Console.WriteLine(f); } } }