// Directory Tree Viewer
using System;
using System.IO;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== Directory Tree Viewer ===");

        try
        {
            Console.Write("Enter directory path: ");
            string path = Console.ReadLine();

            if (!Directory.Exists(path))
            {
                Console.WriteLine("Error: Directory not found!");
                return;
            }

            Console.WriteLine($"\nDirectory tree for: {path}\n");
            PrintDirectory(path, "", true);
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    static void PrintDirectory(string path, string indent, bool isLast)
    {
        Console.WriteLine(indent + (isLast ? "└── " : "├── ") + Path.GetFileName(path));

        try
        {
            var directories = Directory.GetDirectories(path);
            var files = Directory.GetFiles(path);

            string newIndent = indent + (isLast ? "    " : "│   ");

            for (int i = 0; i < directories.Length; i++)
            {
                PrintDirectory(directories[i], newIndent, i == directories.Length - 1 && files.Length == 0);
            }

            for (int i = 0; i < files.Length; i++)
            {
                Console.WriteLine(newIndent + (i == files.Length - 1 ? "└── " : "├── ") + Path.GetFileName(files[i]));
            }
        }
        catch { }
    }
}