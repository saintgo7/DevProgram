// File Writer
using System;
using System.IO;
class Program {
    static void Main() {
        Console.Write("Enter file path: ");
        string path = Console.ReadLine();
        Console.WriteLine("Enter text (type END to finish):");
        using (StreamWriter sw = new StreamWriter(path)) {
            string line;
            while ((line = Console.ReadLine()) != "END") sw.WriteLine(line);
        }
        Console.WriteLine("File saved!");
    }
}