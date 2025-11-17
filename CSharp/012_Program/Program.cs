// File Encryption
using System;
using System.IO;
using System.Text;
class Program { static void Main() { Console.Write("File: "); var file = Console.ReadLine(); var text = File.ReadAllText(file); var encrypted = Convert.ToBase64String(Encoding.UTF8.GetBytes(text)); File.WriteAllText(file + ".enc", encrypted); Console.WriteLine("Encrypted!"); } }