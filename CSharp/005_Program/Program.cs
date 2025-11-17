// File Search
using System;
using System.IO;
class Program {
    static void Main() {
        Console.Write("Directory: ");
        string dir = Console.ReadLine();
        Console.Write("Pattern (*.txt): ");
        string pattern = Console.ReadLine();
        var files = Directory.GetFiles(dir, pattern, SearchOption.AllDirectories);
        Console.WriteLine($"\nFound {files.Length} files");
        foreach (var f in files) Console.WriteLine(f);
    }
}