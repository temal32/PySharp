# PySharp Quick Reference Guide

## Installation & Setup
```python
from pysharp import *
```

## Console Operations
```python
# Output
Console.Write("Hello ")          # No newline
Console.WriteLine("World!")      # With newline
Console.Clear()                  # Clear screen
Console.SetTitle("My App")       # Set window title
Console.Beep()                   # Make sound

# Input
name = Console.ReadLine()        # Read line from user
Console.ReadKey()                # Wait for key press
```

## Math Operations
```python
# Basic operations
result = Math.Max(5, 10)         # Returns 10
result = Math.Min(5, 10)         # Returns 5
result = Math.Abs(-5)            # Returns 5
result = Math.Pow(2, 3)          # Returns 8.0
result = Math.Sqrt(16)           # Returns 4.0

# Rounding
result = Math.Round(3.14159, 2)  # Returns 3.14
result = Math.Floor(3.7)         # Returns 3
result = Math.Ceiling(3.2)       # Returns 4

# Constants
pi_value = Math.PI               # 3.14159...
e_value = Math.E                 # 2.71828...
```

## String Utilities
```python
# Validation
is_empty = String.IsNullOrEmpty(text)
is_whitespace = String.IsNullOrWhiteSpace(text)

# Manipulation
joined = String.Join(", ", ["a", "b", "c"])    # Returns "a, b, c"
formatted = String.Format("Hello {0}!", name)  # Returns "Hello John!"
```

## Type Conversions
```python
# To numbers
number = Convert.ToInt32("42")        # String to int
decimal = Convert.ToDouble("3.14")    # String to float

# To string
text = Convert.ToString(123)          # Number to string

# To boolean
flag = Convert.ToBoolean("true")      # String to bool
```

## File Operations
```python
# Check existence
exists = File.Exists("myfile.txt")

# Read operations
content = File.ReadAllText("file.txt")
lines = File.ReadAllLines("file.txt")

# Write operations
File.WriteAllText("file.txt", "Hello World!")
File.WriteAllLines("file.txt", ["Line 1\n", "Line 2\n"])

# File management
File.Copy("source.txt", "dest.txt")
File.Delete("file.txt")
```

## Directory Operations
```python
# Check existence
exists = Directory.Exists("myfolder")

# Create/Delete
Directory.CreateDirectory("newfolder")
Directory.Delete("oldfolder", recursive=True)

# List contents
files = Directory.GetFiles(".")
folders = Directory.GetDirectories(".")
```

## Path Operations
```python
# Combine paths
full_path = Path.Combine("folder", "subfolder", "file.txt")

# Extract components
filename = Path.GetFileName("/path/to/file.txt")      # "file.txt"
directory = Path.GetDirectoryName("/path/to/file.txt") # "/path/to"
extension = Path.GetExtension("file.txt")             # ".txt"
name_only = Path.GetFileNameWithoutExtension("file.txt") # "file"
```

## Random Numbers
```python
# Random integers
random_int = rnd.Next()              # Any int
random_range = rnd.Next(1, 100)      # Between 1-99
random_double = rnd.NextDouble()     # Between 0.0-1.0

# Random bytes
byte_array = [0] * 10
rnd.NextBytes(byte_array)            # Fill with random bytes
```

## Date and Time
```python
# Current time
now = DateTime.Now()                 # Local time
today = DateTime.Today()             # Today's date
utc_now = DateTime.UtcNow()         # UTC time
```

## Process Management
```python
# Start processes
Process.Start("notepad.exe")         # Start and wait
Process.StartAsync("cmd.exe")        # Start in background

# Process info
pid = Process.GetCurrentProcess()    # Current process ID
```

## Environment Operations
```python
# Directory operations
current = Environment.CurrentDirectory()
Environment.ChangeDirectory("C:\\")

# Environment variables
user = Environment.GetEnvironmentVariable("USERNAME")
Environment.SetEnvironmentVariable("MY_VAR", "value")

# Exit program
Environment.Exit(0)                  # Exit with code 0
```

## Threading
```python
Thread.Sleep(1000)                   # Sleep for 1 second (1000 ms)
Thread.Start("program.exe")          # Start program in new thread
```

## Common Patterns

### Input Validation
```python
Console.Write("Enter a number: ")
input_str = Console.ReadLine()

if not String.IsNullOrEmpty(input_str):
    try:
        number = Convert.ToInt32(input_str)
        Console.WriteLine(f"You entered: {number}")
    except:
        Console.WriteLine("Invalid number!")
```

### File Processing
```python
filename = "data.txt"
if File.Exists(filename):
    content = File.ReadAllText(filename)
    Console.WriteLine(f"File content: {content}")
else:
    Console.WriteLine("File not found!")
```

### Simple Menu System
```python
while True:
    Console.WriteLine("1. Option 1")
    Console.WriteLine("2. Option 2")
    Console.WriteLine("3. Exit")
    Console.Write("Choose: ")
    
    choice = Console.ReadLine()
    
    if choice == "1":
        Console.WriteLine("Option 1 selected")
    elif choice == "2":
        Console.WriteLine("Option 2 selected")
    elif choice == "3":
        break
    else:
        Console.WriteLine("Invalid choice!")
```

### Random Password Generator
```python
def generate_password(length):
    chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789"
    password = ""
    for i in range(length):
        random_index = rnd.Next(0, len(chars))
        password += chars[random_index]
    return password

password = generate_password(12)
Console.WriteLine(f"Generated password: {password}")
```

## Tips and Best Practices

1. **Always use static method calls**: `Console.WriteLine()` not `console.WriteLine()`
2. **Handle exceptions**: Wrap conversions in try-catch blocks
3. **Check file existence**: Use `File.Exists()` before reading files
4. **Clean up resources**: Delete temporary files when done
5. **Use proper data types**: Convert strings to numbers when needed
6. **Cross-platform paths**: Use `Path.Combine()` instead of hardcoded separators

## Debugging Tips

- Use `Console.WriteLine()` for debugging output
- Check return values with `Convert.ToString()`
- Use `File.WriteAllText()` to log debug information
- Test with `test_pysharp.py` to verify functionality
