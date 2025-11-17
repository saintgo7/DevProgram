// INI Config Reader
using System;
using System.IO;
using System.Text.Json;
using System.Collections.Generic;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== INI Config Reader ===");
        Console.WriteLine("Reads INI configuration files\n");

        try
        {
            // Sample data processing
            var data = new Dictionary<string, object>
            {
                { "name", "Sample" },
                { "version", "1.0" },
                { "timestamp", DateTime.Now }
            };

            string json = JsonSerializer.Serialize(data, new JsonSerializerOptions
            {
                WriteIndented = true
            });

            Console.WriteLine("Processed Data:");
            Console.WriteLine(json);

            Console.Write("\nSave to file? (y/n): ");
            if (Console.ReadLine().ToLower() == "y")
            {
                Console.Write("Filename: ");
                string filename = Console.ReadLine();
                File.WriteAllText(filename, json);
                Console.WriteLine($"Saved to {filename}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}