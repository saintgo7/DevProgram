// Directory Lister
using System;
using System.IO;
class Program {
    static void Main() {
        Console.Write("Directory path: ");
        string path = Console.ReadLine();
        if (Directory.Exists(path)) {
            Console.WriteLine("\nFiles:");
            foreach (var file in Directory.GetFiles(path))
                Console.WriteLine($"  {Path.GetFileName(file)}");
            Console.WriteLine("\nDirectories:");
            foreach (var dir in Directory.GetDirectories(path))
                Console.WriteLine($"  {Path.GetFileName(dir)}");
        }
    }
}