// File Size Analyzer
using System;
using System.IO;
using System.Linq;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== File Size Analyzer ===");

        try
        {
            Console.Write("Enter directory path: ");
            string directory = Console.ReadLine();

            if (!Directory.Exists(directory))
            {
                Console.WriteLine("Error: Directory not found!");
                return;
            }

            var files = Directory.GetFiles(directory, "*.*", SearchOption.AllDirectories);

            long totalSize = 0;
            Console.WriteLine("\nFile Size Report:");
            Console.WriteLine("".PadRight(70, '-'));

            var sortedFiles = files
                .Select(f => new { Path = f, Size = new FileInfo(f).Length })
                .OrderByDescending(f => f.Size)
                .ToList();

            foreach (var file in sortedFiles.Take(20))
            {
                totalSize += file.Size;
                string fileName = Path.GetFileName(file.Path);
                string size = FormatSize(file.Size);
                Console.WriteLine($"{fileName,-50} {size,15}");
            }

            Console.WriteLine("".PadRight(70, '-'));
            Console.WriteLine($"Total files: {files.Length}");
            Console.WriteLine($"Total size: {FormatSize(totalSize)}");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    static string FormatSize(long bytes)
    {
        string[] sizes = { "B", "KB", "MB", "GB", "TB" };
        double len = bytes;
        int order = 0;

        while (len >= 1024 && order < sizes.Length - 1)
        {
            order++;
            len = len / 1024;
        }

        return $"{len:0.##} {sizes[order]}";
    }
}
