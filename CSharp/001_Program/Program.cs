// File Reader - Read and display file contents
using System;
using System.IO;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== File Reader ===");
        Console.Write("Enter file path: ");
        string path = Console.ReadLine();
        
        try
        {
            string content = File.ReadAllText(path);
            string[] lines = File.ReadAllLines(path);
            
            Console.WriteLine("\n--- File Contents ---");
            Console.WriteLine(content);
            Console.WriteLine($"\n--- Statistics ---");
            Console.WriteLine($"Total lines: {lines.Length}");
            Console.WriteLine($"Total characters: {content.Length}");
            Console.WriteLine($"File size: {new FileInfo(path).Length} bytes");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
