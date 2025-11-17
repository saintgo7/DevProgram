// URL Validator
using System;
class Program { static void Main() { Console.Write("URL: "); var url = Console.ReadLine(); var valid = Uri.TryCreate(url, UriKind.Absolute, out var uri) && (uri.Scheme == Uri.UriSchemeHttp || uri.Scheme == Uri.UriSchemeHttps); Console.WriteLine(valid ? "Valid!" : "Invalid!"); } }