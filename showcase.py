#!/usr/bin/env python3
"""
PySharp 2.1 - Quick Showcase
Demonstrates the most impressive C# features in Python
"""

from pysharp import *

def showcase():
    """Quick showcase of PySharp 2.1 features"""
    Console.SetTitle("PySharp 2.1 Showcase")
    Console.Clear()
    
    # Header with colors
    Console.WriteLineColored("🚀 PySharp 2.1 - C# Syntax in Python!", ConsoleColor.Cyan)
    Console.WriteLine("=" * 50)
    Console.WriteLine()
    
    # 1. Collections Demo
    Console.WriteSuccess("✅ Collections (Array, List, Dictionary)")
    numbers = [3, 1, 4, 1, 5, 9, 2, 6]
    Console.WriteLine(f"Original numbers: {numbers}")
    Array.Sort(numbers)
    Console.WriteLine(f"Sorted: {numbers}")
    
    students = List()
    students.Add("Alice")
    students.Add("Bob") 
    students.Add("Charlie")
    Console.WriteLine(f"Students: {students.ToArray()}")
    
    grades = Dictionary()
    grades["Alice"] = 95
    grades["Bob"] = 87
    grades["Charlie"] = 92
    Console.WriteLine(f"Alice's grade: {grades['Alice']}")
    Console.WriteLine()
    
    # 2. String Processing
    Console.WriteSuccess("✅ String Processing (StringBuilder, Regex)")
    sb = StringBuilder("Hello")
    sb.Append(" ")
    sb.Append("PySharp")
    sb.AppendLine("!")
    sb.AppendLine("C# syntax in Python is amazing!")
    Console.WriteLine(sb.ToString())
    
    text = "Contact: support@pysharp.com or admin@example.org"
    emails = Regex.Matches(text, r"\b[\w.-]+@[\w.-]+\.\w+\b")
    Console.WriteLine(f"Found emails: {emails}")
    Console.WriteLine()
    
    # 3. JSON and Data
    Console.WriteSuccess("✅ JSON Serialization")
    person = {
        "name": "John Doe",
        "age": 30,
        "skills": ["Python", "C#", "JavaScript"],
        "active": True
    }
    json_string = Json.SerializeIndented(person)
    Console.WriteLine("JSON Output:")
    Console.WriteLine(json_string)
    
    # 4. Time and Performance  
    Console.WriteSuccess("✅ Performance Measurement")
    sw = Stopwatch()
    sw.Start()
    
    # Simulate some work
    large_list = List()
    for i in range(1000):
        large_list.Add(f"Item {i}")
    
    sw.Stop()
    Console.WriteLine(f"⏱️  Created 1000 items in {sw.ElapsedMilliseconds}ms")
    Console.WriteLine()
    
    # 5. Hashing and Security
    Console.WriteSuccess("✅ Cryptographic Hashing")
    secret = "PySharp2.1"
    Console.WriteLine(f"Original: {secret}")
    Console.WriteLine(f"MD5:    {Hash.MD5(secret)}")
    Console.WriteLine(f"SHA256: {Hash.SHA256(secret)}")
    Console.WriteLine()
    
    # 6. GUID Generation
    Console.WriteSuccess("✅ Unique Identifier Generation")
    for i in range(3):
        guid = Guid.NewGuid()
        Console.WriteLine(f"GUID {i+1}: {guid.ToString()}")
    Console.WriteLine()
    
    # 7. Math Operations
    Console.WriteSuccess("✅ Mathematical Operations")
    Console.WriteLine(f"π = {Math.PI:.6f}")
    Console.WriteLine(f"e = {Math.E:.6f}")
    Console.WriteLine(f"2^10 = {Math.Pow(2, 10)}")
    Console.WriteLine(f"√144 = {Math.Sqrt(144)}")
    Console.WriteLine()
    
    # 8. System Information
    Console.WriteSuccess("✅ System Information")
    Console.WriteLine(f"Hostname: {Network.GetHostName()}")
    Console.WriteLine(f"Local IP: {Network.GetLocalIPAddress()}")
    Console.WriteLine(f"Current Directory: {Environment.CurrentDirectory()}")
    Console.WriteLine(f"Process ID: {Process.GetCurrentProcess()}")
    Console.WriteLine()
    
    # 9. Version Information
    Console.WriteSuccess("✅ Version Management")
    pysharp_version = Version(2, 1, 0)
    Console.WriteLine(f"PySharp Version: {pysharp_version.ToString()}")
    Console.WriteLine(f"Current DateTime: {DateTime.Now()}")
    Console.WriteLine()
    
    # 10. Encoding Demo
    Console.WriteSuccess("✅ Text Encoding")
    message = "Hello PySharp! 🚀"
    encoded = Encoding.Base64_Encode(message)
    decoded = Encoding.Base64_Decode(encoded).decode('utf-8')
    Console.WriteLine(f"Original: {message}")
    Console.WriteLine(f"Base64: {encoded}")
    Console.WriteLine(f"Decoded: {decoded}")
    Console.WriteLine()
    
    # Summary
    Console.WriteLineColored("🎉 PySharp 2.1 Summary:", ConsoleColor.Yellow)
    features = [
        "20+ C# classes implemented",
        "500+ methods and properties",
        "Collections: Array, List, Dictionary", 
        "String processing: StringBuilder, Regex",
        "JSON serialization/deserialization",
        "Cryptographic hashing (MD5, SHA256)",
        "Performance measurement tools",
        "Network utilities and system info",
        "Colored console output",
        "Cross-platform compatibility",
        "Zero external dependencies"
    ]
    
    for i, feature in enumerate(features, 1):
        Console.WriteLine(f"  {i:2d}. ✅ {feature}")
    
    Console.WriteLine()
    Console.WriteLineColored("🚀 Ready to use C# syntax in Python!", ConsoleColor.Green)
    Console.WriteLine()
    
    # Code example
    Console.WriteInfo("💡 Quick Example:")
    example_code = '''
from pysharp import *

# C# style coding in Python!
numbers = List()
numbers.Add(42)
numbers.Add(13)
numbers.Add(7)

Console.WriteLine(f"Count: {numbers.Count()}")
Console.WriteSuccess("PySharp rocks!")
'''
    Console.WriteLine(example_code)

if __name__ == "__main__":
    showcase()
    Console.WriteLine("Press Enter to exit...")
    Console.ReadLine()
