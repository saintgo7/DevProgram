// Event Handler
using System;
class Publisher { public event EventHandler DataReceived; public void Trigger() => DataReceived?.Invoke(this, EventArgs.Empty); }
class Program { static void Main() { var pub = new Publisher(); pub.DataReceived += (s, e) => Console.WriteLine("Event received!"); pub.Trigger(); } }