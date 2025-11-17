// Line Counter
using System;
using System.IO;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== Line Counter ===");
        Console.WriteLine("Counts lines in text files");

        try
        {
            Console.Write("Enter file or directory path: ");
            string path = Console.ReadLine();

            if (File.Exists(path))
            {
                ProcessFile(path);
            }
            else if (Directory.Exists(path))
            {
                ProcessDirectory(path);
            }
            else
            {
                Console.WriteLine("Error: Path not found!");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    static void ProcessFile(string file)
    {
        FileInfo info = new FileInfo(file);
        Console.WriteLine($"\nFile: {Path.GetFileName(file)}");
        Console.WriteLine($"Size: {info.Length:N0} bytes");
        Console.WriteLine($"Created: {info.CreationTime}");
        Console.WriteLine($"Modified: {info.LastWriteTime}");
    }

    static void ProcessDirectory(string directory)
    {
        var files = Directory.GetFiles(directory);
        Console.WriteLine($"\nFound {files.Length} files in directory");

        foreach (var file in files)
        {
            Console.WriteLine($"  {Path.GetFileName(file)}");
        }
    }
}