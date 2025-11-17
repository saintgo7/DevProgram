// SQL Query Builder
using System;
class Program { static void Main() { Console.Write("Table: "); var table = Console.ReadLine(); Console.Write("Column: "); var col = Console.ReadLine(); Console.Write("Value: "); var val = Console.ReadLine(); Console.WriteLine($"SELECT * FROM {table} WHERE {col} = '{val}'"); } }