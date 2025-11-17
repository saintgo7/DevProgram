// Delegate Example
using System;
delegate void PrintDelegate(string msg);
class Program { static void Main() { PrintDelegate print = Console.WriteLine; print("Hello from delegate!"); } }