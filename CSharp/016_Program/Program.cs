// File Rename Tool
using System;
using System.IO;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== File Rename Tool ===");

        try
        {
            Console.Write("Enter directory path: ");
            string directory = Console.ReadLine();

            if (!Directory.Exists(directory))
            {
                Console.WriteLine("Error: Directory not found!");
                return;
            }

            Console.Write("Enter search pattern (*.txt): ");
            string pattern = Console.ReadLine();

            Console.Write("Enter prefix to add: ");
            string prefix = Console.ReadLine();

            var files = Directory.GetFiles(directory, pattern);

            Console.WriteLine($"\nFound {files.Length} files:");

            foreach (var file in files)
            {
                string fileName = Path.GetFileName(file);
                string newFileName = prefix + fileName;
                string newPath = Path.Combine(directory, newFileName);

                File.Move(file, newPath);
                Console.WriteLine($"Renamed: {fileName} -> {newFileName}");
            }

            Console.WriteLine($"\nRenamed {files.Length} files successfully!");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}
