// CSV Writer
using System;
using System.IO;
class Program { static void Main() { using (var sw = new StreamWriter("output.csv")) { sw.WriteLine("Name,Age,City"); sw.WriteLine("John,30,NYC"); sw.WriteLine("Jane,25,LA"); } Console.WriteLine("CSV created!"); } }