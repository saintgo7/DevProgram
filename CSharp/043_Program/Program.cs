// XML Parser
using System;
using System.Xml;
class Program { static void Main() { var xml = "<person><name>John</name></person>"; var doc = new XmlDocument(); doc.LoadXml(xml); Console.WriteLine(doc.SelectSingleNode("//name").InnerText); } }