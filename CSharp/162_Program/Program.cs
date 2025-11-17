// Parallel Processing
using System;
using System.Linq;
using System.Threading.Tasks;
class Program { static void Main() { var numbers = Enumerable.Range(1, 100); Parallel.ForEach(numbers, n => Console.WriteLine($"Processing {n} on thread {Task.CurrentId}")); } }