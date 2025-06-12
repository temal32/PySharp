from pysharp import *

# ========================================
# PySharp Version 2.0 - C# Syntax in Python
# ========================================

def main():
    # Console Operations
    Console.SetTitle("PySharp Demo - C# Syntax in Python!")
    Console.WriteLine("=== PySharp Version 2.0 Demo ===")
    Console.WriteLine()
    
    # String operations
    name = "PySharp"
    version = "2.0"
    message = String.Format("Welcome to {0} version {1}!", name, version)
    Console.WriteLine(message)
    Console.WriteLine()
    
    # Math operations
    Console.WriteLine("=== Math Operations ===")
    num1 = 10
    num2 = 3
    Console.WriteLine(f"Max({num1}, {num2}) = {Math.Max(num1, num2)}")
    Console.WriteLine(f"Min({num1}, {num2}) = {Math.Min(num1, num2)}")
    Console.WriteLine(f"Pow({num1}, {num2}) = {Math.Pow(num1, num2)}")
    Console.WriteLine(f"Sqrt({num1}) = {Math.Round(Math.Sqrt(num1), 2)}")
    Console.WriteLine(f"PI = {Math.PI}")
    Console.WriteLine()
    
    # Random numbers
    Console.WriteLine("=== Random Numbers ===")
    for i in range(5):
        randomNum = rnd.Next(1, 101)  # Random number between 1-100
        Console.WriteLine(f"Random number {i+1}: {randomNum}")
    Console.WriteLine()
    
    # Date and Time
    Console.WriteLine("=== Date and Time ===")
    now = DateTime.Now()
    today = DateTime.Today()
    Console.WriteLine(f"Current DateTime: {now}")
    Console.WriteLine(f"Today's Date: {today}")
    Console.WriteLine()
    
    # File operations example
    Console.WriteLine("=== File Operations ===")
    testFile = "test.txt"
    testContent = "Hello from PySharp!\nThis is a test file."
    
    File.WriteAllText(testFile, testContent)
    Console.WriteLine(f"Created file: {testFile}")
    
    if File.Exists(testFile):
        content = File.ReadAllText(testFile)
        Console.WriteLine(f"File content:\n{content}")
    Console.WriteLine()
    
    # Directory operations
    Console.WriteLine("=== Directory Operations ===")
    currentDir = Environment.CurrentDirectory()
    Console.WriteLine(f"Current Directory: {currentDir}")
    
    # Path operations
    filePath = Path.Combine(currentDir, testFile)
    fileName = Path.GetFileName(filePath)
    fileExt = Path.GetExtension(filePath)
    Console.WriteLine(f"Full Path: {filePath}")
    Console.WriteLine(f"File Name: {fileName}")
    Console.WriteLine(f"Extension: {fileExt}")
    Console.WriteLine()
    
    # Conversion operations
    Console.WriteLine("=== Type Conversions ===")
    stringNumber = "42"
    numberFromString = Convert.ToInt32(stringNumber)
    Console.WriteLine(f"String '{stringNumber}' converted to int: {numberFromString}")
    
    doubleValue = 3.14159
    roundedValue = Math.Round(doubleValue, 2)
    Console.WriteLine(f"Double {doubleValue} rounded to 2 decimals: {roundedValue}")
    Console.WriteLine()
    
    # String utilities
    Console.WriteLine("=== String Utilities ===")
    emptyStr = ""
    nullStr = None
    normalStr = "Hello World"
    
    Console.WriteLine(f"IsNullOrEmpty(''): {String.IsNullOrEmpty(emptyStr)}")
    Console.WriteLine(f"IsNullOrEmpty(None): {String.IsNullOrEmpty(nullStr)}")
    Console.WriteLine(f"IsNullOrEmpty('Hello World'): {String.IsNullOrEmpty(normalStr)}")
    
    words = ["Python", "meets", "C#", "syntax"]
    joinedStr = String.Join(" ", words)
    Console.WriteLine(f"Joined string: {joinedStr}")
    Console.WriteLine()
    
    # Interactive section
    Console.WriteLine("=== Interactive Section ===")
    Console.Write("Enter your name: ")
    userName = Console.ReadLine()
    
    if not String.IsNullOrEmpty(userName):
        greeting = String.Format("Hello, {0}! Nice to meet you.", userName)
        Console.WriteLine(greeting)
    else:
        Console.WriteLine("You didn't enter a name!")
    
    Console.WriteLine()
    Console.WriteLine("Press Enter to continue with process demo...")
    Console.ReadLine()
    
    # Process operations
    Console.WriteLine("=== Process Operations ===")
    Console.WriteLine("Opening notepad...")
    Process.StartAsync("notepad.exe")
    
    Console.WriteLine("Current Process ID: " + Convert.ToString(Process.GetCurrentProcess()))
    Console.WriteLine()
    
    # Cleanup
    if File.Exists(testFile):
        File.Delete(testFile)
        Console.WriteLine(f"Cleaned up: {testFile}")
    
    # Countdown before exit
    Console.WriteLine()
    Console.WriteLine("Program will exit in 3 seconds...")
    for i in range(3, 0, -1):
        Console.Write(f"{i}... ")
        Thread.Sleep(1000)
    Console.WriteLine()
    
    Console.WriteLine("Thanks for trying PySharp!")
    Console.Beep()
    
    # Exit with success code
    Environment.Exit(0)

# Call main function like in C#
if __name__ == "__main__":
    main()