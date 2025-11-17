// File Copy Tool
using System;
using System.IO;
class Program {
    static void Main() {
        Console.Write("Source: ");
        string src = Console.ReadLine();
        Console.Write("Destination: ");
        string dest = Console.ReadLine();
        try {
            File.Copy(src, dest, true);
            Console.WriteLine("Copied successfully!");
        } catch (Exception ex) {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}