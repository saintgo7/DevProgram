// File Decryption
using System;
using System.IO;
using System.Text;
class Program { static void Main() { Console.Write("Encrypted file: "); var file = Console.ReadLine(); var encrypted = File.ReadAllText(file); var decrypted = Encoding.UTF8.GetString(Convert.FromBase64String(encrypted)); Console.WriteLine(decrypted); } }