from pysharp import *

# ========================================
# PySharp Examples - Various Use Cases
# ========================================

def basic_console_example():
    """Basic console input/output like C#"""
    Console.WriteLine("=== Basic Console Example ===")
    Console.Write("Enter your age: ")
    ageStr = Console.ReadLine()
    age = Convert.ToInt32(ageStr)
    
    if age >= 18:
        Console.WriteLine("You are an adult!")
    else:
        Console.WriteLine("You are a minor!")
    Console.WriteLine()

def file_processing_example():
    """File processing like C#"""
    Console.WriteLine("=== File Processing Example ===")
    
    # Create a sample data file
    data = ["Name,Age,City", "John,25,New York", "Jane,30,Los Angeles", "Bob,22,Chicago"]
    File.WriteAllLines("data.csv", [line + "\n" for line in data])
    
    # Read and process the file
    if File.Exists("data.csv"):
        lines = File.ReadAllLines("data.csv")
        Console.WriteLine("CSV Data:")
        for line in lines:
            Console.WriteLine(line.strip())
    
    # Clean up
    File.Delete("data.csv")
    Console.WriteLine("File processed and cleaned up!")
    Console.WriteLine()

def math_calculator_example():
    """Simple calculator using Math class"""
    Console.WriteLine("=== Math Calculator Example ===")
    
    while True:
        Console.Write("Enter first number (or 'quit' to exit): ")
        input1 = Console.ReadLine()
        
        if input1.lower() == "quit":
            break
            
        Console.Write("Enter second number: ")
        input2 = Console.ReadLine()
        
        try:
            num1 = Convert.ToDouble(input1)
            num2 = Convert.ToDouble(input2)
            
            Console.WriteLine(f"Addition: {num1} + {num2} = {num1 + num2}")
            Console.WriteLine(f"Subtraction: {num1} - {num2} = {num1 - num2}")
            Console.WriteLine(f"Multiplication: {num1} * {num2} = {num1 * num2}")
            if num2 != 0:
                Console.WriteLine(f"Division: {num1} / {num2} = {num1 / num2}")
            Console.WriteLine(f"Power: {num1} ^ {num2} = {Math.Pow(num1, num2)}")
            Console.WriteLine(f"Max: {Math.Max(num1, num2)}")
            Console.WriteLine(f"Min: {Math.Min(num1, num2)}")
            Console.WriteLine()
            
        except Exception as e:
            Console.WriteLine(f"Error: Invalid input - {e}")
            Console.WriteLine()

def random_password_generator():
    """Generate random passwords"""
    Console.WriteLine("=== Random Password Generator ===")
    
    Console.Write("Enter password length: ")
    lengthStr = Console.ReadLine()
    length = Convert.ToInt32(lengthStr)
    
    # Characters to use in password
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*"
    password = ""
    
    for i in range(length):
        randomIndex = rnd.Next(0, len(chars))
        password += chars[randomIndex]
    
    Console.WriteLine(f"Generated password: {password}")
    Console.WriteLine()

def directory_explorer():
    """Simple directory explorer"""
    Console.WriteLine("=== Directory Explorer ===")
    
    currentPath = Environment.CurrentDirectory()
    Console.WriteLine(f"Current directory: {currentPath}")
    
    while True:
        Console.WriteLine("\nOptions:")
        Console.WriteLine("1. List files")
        Console.WriteLine("2. List directories")
        Console.WriteLine("3. Change directory")
        Console.WriteLine("4. Create directory")
        Console.WriteLine("5. Exit")
        Console.Write("Choose option: ")
        
        choice = Console.ReadLine()
        
        if choice == "1":
            files = Directory.GetFiles(currentPath)
            Console.WriteLine("Files:")
            for file in files:
                fileName = Path.GetFileName(file)
                Console.WriteLine(f"  {fileName}")
                
        elif choice == "2":
            dirs = Directory.GetDirectories(currentPath)
            Console.WriteLine("Directories:")
            for dir in dirs:
                Console.WriteLine(f"  {dir}")
                
        elif choice == "3":
            Console.Write("Enter directory path: ")
            newPath = Console.ReadLine()
            if Directory.Exists(newPath):
                Environment.ChangeDirectory(newPath)
                currentPath = Environment.CurrentDirectory()
                Console.WriteLine(f"Changed to: {currentPath}")
            else:
                Console.WriteLine("Directory does not exist!")
                
        elif choice == "4":
            Console.Write("Enter directory name: ")
            dirName = Console.ReadLine()
            if not String.IsNullOrEmpty(dirName):
                Directory.CreateDirectory(dirName)
                Console.WriteLine(f"Created directory: {dirName}")
            else:
                Console.WriteLine("Invalid directory name!")
                
        elif choice == "5":
            break
        else:
            Console.WriteLine("Invalid option!")

def string_utilities_demo():
    """Demonstrate string utilities"""
    Console.WriteLine("=== String Utilities Demo ===")
    
    # Get input
    Console.Write("Enter some text: ")
    text = Console.ReadLine()
    
    # String analysis
    Console.WriteLine(f"Original text: '{text}'")
    Console.WriteLine(f"Length: {len(text)}")
    Console.WriteLine(f"Is null or empty: {String.IsNullOrEmpty(text)}")
    Console.WriteLine(f"Is null or whitespace: {String.IsNullOrWhiteSpace(text)}")
    Console.WriteLine(f"Uppercase: {text.upper()}")
    Console.WriteLine(f"Lowercase: {text.lower()}")
    
    # Split and join
    if not String.IsNullOrEmpty(text):
        words = text.split()
        Console.WriteLine(f"Word count: {len(words)}")
        Console.WriteLine("Words:")
        for i, word in enumerate(words):
            Console.WriteLine(f"  {i+1}. {word}")
        
        # Join with different separators
        joined = String.Join(" | ", words)
        Console.WriteLine(f"Joined with ' | ': {joined}")
    
    Console.WriteLine()

def system_info_demo():
    """Display system information"""
    Console.WriteLine("=== System Information ===")
    
    Console.WriteLine(f"Current Process ID: {Process.GetCurrentProcess()}")
    Console.WriteLine(f"Current Directory: {Environment.CurrentDirectory()}")
    Console.WriteLine(f"Current Date/Time: {DateTime.Now()}")
    Console.WriteLine(f"Today's Date: {DateTime.Today()}")
    Console.WriteLine(f"UTC Time: {DateTime.UtcNow()}")
    
    # Environment variables
    Console.WriteLine("Some Environment Variables:")
    important_vars = ["PATH", "USERNAME", "COMPUTERNAME", "OS"]
    for var in important_vars:
        value = Environment.GetEnvironmentVariable(var)
        if value:
            # Truncate long values
            display_value = value[:50] + "..." if len(value) > 50 else value
            Console.WriteLine(f"  {var}: {display_value}")
    
    Console.WriteLine()

def main():
    """Main function to run all examples"""
    Console.SetTitle("PySharp Examples")
    Console.Clear()
    
    while True:
        Console.WriteLine("=== PySharp Examples Menu ===")
        Console.WriteLine("1. Basic Console Example")
        Console.WriteLine("2. File Processing Example")
        Console.WriteLine("3. Math Calculator")
        Console.WriteLine("4. Random Password Generator")
        Console.WriteLine("5. Directory Explorer")
        Console.WriteLine("6. String Utilities Demo")
        Console.WriteLine("7. System Information")
        Console.WriteLine("8. Clear Screen")
        Console.WriteLine("9. Exit")
        Console.WriteLine()
        Console.Write("Choose an example (1-9): ")
        
        choice = Console.ReadLine()
        Console.WriteLine()
        
        try:
            if choice == "1":
                basic_console_example()
            elif choice == "2":
                file_processing_example()
            elif choice == "3":
                math_calculator_example()
            elif choice == "4":
                random_password_generator()
            elif choice == "5":
                directory_explorer()
            elif choice == "6":
                string_utilities_demo()
            elif choice == "7":
                system_info_demo()
            elif choice == "8":
                Console.Clear()
                continue
            elif choice == "9":
                Console.WriteLine("Thanks for trying PySharp examples!")
                break
            else:
                Console.WriteLine("Invalid choice! Please select 1-9.")
        
        except Exception as e:
            Console.WriteLine(f"An error occurred: {e}")
        
        Console.WriteLine("Press Enter to continue...")
        Console.ReadLine()
        Console.WriteLine()

if __name__ == "__main__":
    main()
