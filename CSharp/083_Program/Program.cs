// REST API Call
using System;
using System.Net.Http;
using System.Threading.Tasks;
class Program { static async Task Main() { using var client = new HttpClient(); var json = await client.GetStringAsync("https://jsonplaceholder.typicode.com/posts/1"); Console.WriteLine(json); } }