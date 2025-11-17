// Advanced Tool 178
using System;
using System.Threading.Tasks;
using System.Linq;

class Program
{
    static async Task Main()
    {
        Console.WriteLine("=== Advanced Tool 178 ===");
        Console.WriteLine("Advanced system tool 178\n");

        try
        {
            // Demonstrate async operation
            Console.WriteLine("Processing...");

            var tasks = Enumerable.Range(1, 5).Select(i => ProcessAsync(i));
            await Task.WhenAll(tasks);

            Console.WriteLine("\nAll tasks completed!");
        }
        catch (Exception ex)
        {
            Console.WriteLine($"Error: {ex.Message}");
        }
    }

    static async Task ProcessAsync(int id)
    {
        await Task.Delay(100 * id);
        Console.WriteLine($"Task {id} completed");
    }
}