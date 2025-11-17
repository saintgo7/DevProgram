// Web Download
using System;
using System.Net;
class Program { static void Main() { Console.Write("URL: "); var url = Console.ReadLine(); Console.Write("Save as: "); var file = Console.ReadLine(); new WebClient().DownloadFile(url, file); Console.WriteLine("Downloaded!"); } }