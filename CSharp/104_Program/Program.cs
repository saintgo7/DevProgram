// Network Tool 104
using System;
using System.Net;
using System.Net.Http;
using System.Threading.Tasks;

class Program
{
    static async Task Main()
    {
        Console.WriteLine("=== Network Tool 104 ===");
        Console.WriteLine("Network utility tool 104\n");

        try
        {
            Console.Write("Enter URL: ");
            string url = Console.ReadLine();

            using (HttpClient client = new HttpClient())
            {
                Console.WriteLine("Fetching...");
                var response = await client.GetAsync(url);

                Console.WriteLine($"\nStatus: {response.StatusCode}");
                Console.WriteLine($"Content-Type: {response.Content.Headers.ContentType}");

                string content = await response.Content.ReadAsStringAsync();
                Console.WriteLine($"\nContent (first 500 chars):");
                Console.WriteLine(content.Substring(0, Math.Min(500, content.Length)));
            }
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }
}