// File Compression Tool
using System;
using System.IO;
using System.IO.Compression;

class Program
{
    static void Main()
    {
        Console.WriteLine("=== File Compression Tool ===");
        Console.WriteLine("1. Compress file");
        Console.WriteLine("2. Decompress file");
        Console.Write("Choice: ");

        string choice = Console.ReadLine();

        try
        {
            if (choice == "1")
            {
                Console.Write("Source file: ");
                string source = Console.ReadLine();
                string output = source + ".gz";

                using (FileStream sourceStream = File.OpenRead(source))
                using (FileStream targetStream = File.Create(output))
                using (GZipStream compressionStream = new GZipStream(targetStream, CompressionMode.Compress))
                {
                    sourceStream.CopyTo(compressionStream);
                }

                long original = new FileInfo(source).Length;
                long compressed = new FileInfo(output).Length;
                double ratio = (1.0 - (double)compressed / original) * 100;

                Console.WriteLine($"\nCompressed: {output}");
                Console.WriteLine($"Original size: {original:N0} bytes");
                Console.WriteLine($"Compressed size: {compressed:N0} bytes");
                Console.WriteLine($"Compression ratio: {ratio:F2}%");
            }
            else
            {
                Console.Write("Compressed file (.gz): ");
                string source = Console.ReadLine();
                string output = source.Replace(".gz", "");

                using (FileStream sourceStream = File.OpenRead(source))
                using (FileStream targetStream = File.Create(output))
                using (GZipStream decompressionStream = new GZipStream(sourceStream, CompressionMode.Decompress))
                {
                    decompressionStream.CopyTo(targetStream);
                }

                Console.WriteLine($"\nDecompressed: {output}");
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}