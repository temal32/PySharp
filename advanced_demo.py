from pysharp import *

# ========================================
# PySharp Version 2.1 - Advanced C# Features Demo
# ========================================

def demo_collections():
    """Demonstrate C# collection classes"""
    Console.WriteLineColored("=== Collections Demo ===", ConsoleColor.Cyan)
    
    # Array operations
    Console.WriteLine("Array Operations:")
    numbers = [5, 2, 8, 1, 9]
    Console.WriteLine(f"Original: {numbers}")
    Array.Sort(numbers)
    Console.WriteLine(f"Sorted: {numbers}")
    Array.Reverse(numbers)
    Console.WriteLine(f"Reversed: {numbers}")
    Console.WriteLine(f"Contains 8: {Array.Contains(numbers, 8)}")
    Console.WriteLine()
    
    # List operations
    Console.WriteLine("List Operations:")
    fruits = List()
    fruits.Add("apple")
    fruits.Add("banana")
    fruits.Add("cherry")
    fruits.Insert(1, "orange")
    
    Console.WriteLine(f"List count: {fruits.Count()}")
    Console.WriteLine("Fruits:")
    for i in range(fruits.Count()):
        Console.WriteLine(f"  {i}: {fruits[i]}")
    
    fruits.Remove("banana")
    Console.WriteLine(f"After removing banana: {fruits.ToArray()}")
    Console.WriteLine()
    
    # Dictionary operations
    Console.WriteLine("Dictionary Operations:")
    person = Dictionary()
    person.Add("name", "John Doe")
    person.Add("age", 30)
    person.Add("city", "New York")
    person["country"] = "USA"  # Using indexer
    
    Console.WriteLine(f"Person count: {person.Count()}")
    Console.WriteLine("Person details:")
    for key in person.Keys():
        Console.WriteLine(f"  {key}: {person[key]}")
    
    success, name = person.TryGetValue("name")
    if success:
        Console.WriteLine(f"Name retrieved: {name}")
    Console.WriteLine()

def demo_string_processing():
    """Demonstrate string processing capabilities"""
    Console.WriteLineColored("=== String Processing Demo ===", ConsoleColor.Green)
    
    # StringBuilder
    Console.WriteLine("StringBuilder:")
    sb = StringBuilder("Hello")
    sb.Append(" ")
    sb.Append("PySharp")
    sb.AppendLine("!")
    sb.AppendLine("Welcome to advanced string building.")
    sb.Replace("PySharp", "C# in Python")
    
    result = sb.ToString()
    Console.WriteLine("Built string:")
    Console.WriteLine(result)
    
    # Regular expressions
    Console.WriteLine("Regular Expressions:")
    text = "Contact us at support@pysharp.com or info@example.org"
    
    if Regex.IsMatch(text, r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"):
        Console.WriteLine("✅ Email addresses found!")
        
    emails = Regex.Matches(text, r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b")
    Console.WriteLine("Email addresses:")
    for email in emails:
        Console.WriteLine(f"  📧 {email}")
    
    # Replace emails with placeholder
    censored = Regex.Replace(text, r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", "[EMAIL]")
    Console.WriteLine(f"Censored: {censored}")
    Console.WriteLine()

def demo_time_and_dates():
    """Demonstrate time and date functionality"""
    Console.WriteLineColored("=== Time and Dates Demo ===", ConsoleColor.Yellow)
    
    # DateTime operations
    now = DateTime.Now()
    today = DateTime.Today()
    utc_now = DateTime.UtcNow()
    
    Console.WriteLine(f"Current time: {now}")
    Console.WriteLine(f"Today's date: {today}")
    Console.WriteLine(f"UTC time: {utc_now}")
    Console.WriteLine()
    
    # TimeSpan operations
    Console.WriteLine("TimeSpan Operations:")
    duration = TimeSpan(days=2, hours=3, minutes=30, seconds=45)
    Console.WriteLine(f"Duration: {duration.ToString()}")
    Console.WriteLine(f"Total hours: {duration.TotalHours:.2f}")
    Console.WriteLine(f"Total minutes: {duration.TotalMinutes:.0f}")
    Console.WriteLine(f"Total seconds: {duration.TotalSeconds:.0f}")
    
    # Create TimeSpan from different units
    one_day = TimeSpan.FromDays(1)
    two_hours = TimeSpan.FromHours(2)
    thirty_minutes = TimeSpan.FromMinutes(30)
    
    Console.WriteLine(f"One day: {one_day.ToString()}")
    Console.WriteLine(f"Two hours: {two_hours.ToString()}")
    Console.WriteLine(f"Thirty minutes: {thirty_minutes.ToString()}")
    Console.WriteLine()

def demo_guid_and_versioning():
    """Demonstrate GUID and version handling"""
    Console.WriteLineColored("=== GUID and Versioning Demo ===", ConsoleColor.Magenta)
    
    # GUID operations
    Console.WriteLine("GUID Operations:")
    guid1 = Guid.NewGuid()
    guid2 = Guid.NewGuid()
    empty_guid = Guid.Empty()
    
    Console.WriteLine(f"New GUID 1: {guid1.ToString()}")
    Console.WriteLine(f"New GUID 2: {guid2.ToString()}")
    Console.WriteLine(f"Empty GUID: {empty_guid.ToString()}")
    
    # Parse existing GUID
    known_guid = Guid("550e8400-e29b-41d4-a716-446655440000")
    Console.WriteLine(f"Parsed GUID: {known_guid.ToString()}")
    Console.WriteLine()
    
    # Version operations
    Console.WriteLine("Version Operations:")
    pysharp_version = Version(2, 1, 0, 0)
    Console.WriteLine(f"PySharp version: {pysharp_version.ToString()}")
    
    parsed_version = Version.Parse("3.2.1.4")
    Console.WriteLine(f"Parsed version: {parsed_version.ToString()}")
    Console.WriteLine(f"Major: {parsed_version.Major}, Minor: {parsed_version.Minor}")
    Console.WriteLine()

def demo_encoding_and_hashing():
    """Demonstrate encoding and hashing capabilities"""
    Console.WriteLineColored("=== Encoding and Hashing Demo ===", ConsoleColor.Blue)
    
    secret_message = "PySharp is awesome! 🚀"
    
    # Encoding operations
    Console.WriteLine("Encoding Operations:")
    utf8_bytes = Encoding.UTF8_GetBytes(secret_message)
    Console.WriteLine(f"UTF-8 bytes length: {len(utf8_bytes)}")
    
    # Base64 encoding
    base64_encoded = Encoding.Base64_Encode(secret_message)
    Console.WriteLine(f"Base64 encoded: {base64_encoded}")
    
    base64_decoded = Encoding.Base64_Decode(base64_encoded).decode('utf-8')
    Console.WriteLine(f"Base64 decoded: {base64_decoded}")
    Console.WriteLine()
    
    # Hashing operations
    Console.WriteLine("Hashing Operations:")
    test_data = "Hello PySharp!"
    
    md5_hash = Hash.MD5(test_data)
    sha1_hash = Hash.SHA1(test_data)
    sha256_hash = Hash.SHA256(test_data)
    
    Console.WriteLine(f"Original: {test_data}")
    Console.WriteLine(f"MD5:    {md5_hash}")
    Console.WriteLine(f"SHA1:   {sha1_hash}")
    Console.WriteLine(f"SHA256: {sha256_hash}")
    Console.WriteLine()

def demo_json_and_data():
    """Demonstrate JSON and data handling"""
    Console.WriteLineColored("=== JSON and Data Demo ===", ConsoleColor.Red)
    
    # Create sample data
    student_data = {
        "name": "Alice Johnson",
        "age": 22,
        "major": "Computer Science",
        "grades": [95, 87, 92, 98],
        "graduated": False,
        "contact": {
            "email": "alice@university.edu",
            "phone": "555-0123"
        }
    }
    
    # JSON serialization
    Console.WriteLine("JSON Operations:")
    json_string = Json.Serialize(student_data)
    Console.WriteLine("Compact JSON:")
    Console.WriteLine(json_string)
    Console.WriteLine()
    
    # Formatted JSON
    formatted_json = Json.SerializeIndented(student_data)
    Console.WriteLine("Formatted JSON:")
    Console.WriteLine(formatted_json)
    Console.WriteLine()
    
    # JSON deserialization
    parsed_data = Json.Deserialize(json_string)
    Console.WriteLine("Parsed data:")
    Console.WriteLine(f"Name: {parsed_data['name']}")
    Console.WriteLine(f"Age: {parsed_data['age']}")
    Console.WriteLine(f"Average grade: {sum(parsed_data['grades']) / len(parsed_data['grades']):.1f}")
    Console.WriteLine()

def demo_performance_and_utilities():
    """Demonstrate performance measurement and utilities"""
    Console.WriteLineColored("=== Performance and Utilities Demo ===", ConsoleColor.DarkGreen)
    
    # Stopwatch for performance measurement
    Console.WriteLine("Performance Measurement:")
    sw = Stopwatch()
    
    sw.Start()
    Console.WriteLine("Performing some work...")
    
    # Simulate work with array operations
    large_array = list(range(1000))
    Array.Reverse(large_array)
    Array.Sort(large_array)
    
    Thread.Sleep(100)  # Simulate additional work
    
    sw.Stop()
    Console.WriteLine(f"⏱️  Operation completed in {sw.ElapsedMilliseconds}ms")
    Console.WriteLine(f"   ({sw.ElapsedSeconds:.3f} seconds)")
    Console.WriteLine()
    
    # Network utilities
    Console.WriteLine("Network Information:")
    try:
        hostname = Network.GetHostName()
        local_ip = Network.GetLocalIPAddress()
        Console.WriteLine(f"Hostname: {hostname}")
        Console.WriteLine(f"Local IP: {local_ip}")
        
        # Test ping
        Console.Write("Testing ping to google.com... ")
        if Network.Ping("google.com", timeout=2):
            Console.WriteSuccess("✅ Success")
        else:
            Console.WriteError("❌ Failed")
    except Exception as e:
        Console.WriteLine(f"Network info unavailable: {e}")
    Console.WriteLine()
    
    # BitConverter operations
    Console.WriteLine("BitConverter Operations:")
    number = 42
    float_number = 3.14159
    
    number_bytes = BitConverter.GetBytes(number)
    float_bytes = BitConverter.GetBytes(float_number)
    
    Console.WriteLine(f"Number {number} as bytes: {BitConverter.ToString(number_bytes)}")
    Console.WriteLine(f"Float {float_number} as bytes: {BitConverter.ToString(float_bytes)}")
    
    # Convert back
    converted_number = BitConverter.ToInt32(number_bytes)
    Console.WriteLine(f"Converted back: {converted_number}")
    Console.WriteLine()

def demo_advanced_console():
    """Demonstrate advanced console features"""
    Console.WriteLineColored("=== Advanced Console Demo ===", ConsoleColor.White)
    
    # Colored output
    Console.WriteLine("Colored Console Output:")
    Console.WriteError("❌ This is an error message")
    Console.WriteWarning("⚠️  This is a warning message")
    Console.WriteSuccess("✅ This is a success message")
    Console.WriteInfo("ℹ️  This is an info message")
    
    Console.WriteLine()
    Console.WriteLine("All available colors:")
    colors = [
        (ConsoleColor.Red, "Red"),
        (ConsoleColor.Green, "Green"),
        (ConsoleColor.Blue, "Blue"),
        (ConsoleColor.Yellow, "Yellow"),
        (ConsoleColor.Magenta, "Magenta"),
        (ConsoleColor.Cyan, "Cyan"),
        (ConsoleColor.White, "White"),
        (ConsoleColor.DarkRed, "DarkRed"),
        (ConsoleColor.DarkGreen, "DarkGreen"),
        (ConsoleColor.DarkBlue, "DarkBlue")
    ]
    
    for color, name in colors:
        Console.WriteColored(f"■ {name} ", color)
    Console.WriteLine()
    Console.WriteLine()

def interactive_demo():
    """Interactive demonstration"""
    Console.WriteLineColored("=== Interactive Demo ===", ConsoleColor.Cyan)
    
    Console.WriteLine("Let's create a simple contact manager!")
    contacts = Dictionary()
    
    while True:
        Console.WriteLine("\nContact Manager Options:")
        Console.WriteLine("1. Add contact")
        Console.WriteLine("2. List contacts")
        Console.WriteLine("3. Search contact")
        Console.WriteLine("4. Export to JSON")
        Console.WriteLine("5. Exit")
        Console.Write("Choose option: ")
        
        choice = Console.ReadLine()
        
        if choice == "1":
            Console.Write("Enter name: ")
            name = Console.ReadLine()
            Console.Write("Enter email: ")
            email = Console.ReadLine()
            Console.Write("Enter phone: ")
            phone = Console.ReadLine()
            
            contact_info = {"email": email, "phone": phone}
            contacts[name] = contact_info
            Console.WriteSuccess(f"✅ Contact '{name}' added!")
            
        elif choice == "2":
            if contacts.Count() == 0:
                Console.WriteWarning("No contacts found.")
            else:
                Console.WriteLine(f"\nAll Contacts ({contacts.Count()}):")
                for name in contacts.Keys():
                    info = contacts[name]
                    Console.WriteLine(f"📧 {name}")
                    Console.WriteLine(f"   Email: {info['email']}")
                    Console.WriteLine(f"   Phone: {info['phone']}")
                    
        elif choice == "3":
            if contacts.Count() == 0:
                Console.WriteWarning("No contacts to search.")
                continue
                
            Console.Write("Enter name to search: ")
            search_name = Console.ReadLine()
            
            if contacts.ContainsKey(search_name):
                info = contacts[search_name]
                Console.WriteSuccess(f"Found: {search_name}")
                Console.WriteLine(f"Email: {info['email']}")
                Console.WriteLine(f"Phone: {info['phone']}")
            else:
                Console.WriteError("Contact not found.")
                
        elif choice == "4":
            if contacts.Count() == 0:
                Console.WriteWarning("No contacts to export.")
                continue
                
            # Convert to regular dict for JSON serialization
            export_data = {}
            for name in contacts.Keys():
                export_data[name] = contacts[name]
                
            json_data = Json.SerializeIndented(export_data)
            timestamp = DateTime.Now().strftime("%Y%m%d_%H%M%S")
            filename = f"contacts_{timestamp}.json"
            
            File.WriteAllText(filename, json_data)
            Console.WriteSuccess(f"✅ Contacts exported to {filename}")
            
        elif choice == "5":
            Console.WriteLine("Thanks for using PySharp Contact Manager!")
            break
        else:
            Console.WriteError("Invalid option!")

def main():
    """Main demonstration function"""
    Console.SetTitle("PySharp 2.1 - Advanced C# Features")
    Console.Clear()
    
    Console.WriteLineColored("🚀 PySharp Version 2.1 - Advanced C# Features Demo", ConsoleColor.White)
    Console.WriteLine("=" * 60)
    Console.WriteLine()
    
    demos = [
        ("Collections (Array, List, Dictionary)", demo_collections),
        ("String Processing (StringBuilder, Regex)", demo_string_processing),
        ("Time and Dates (DateTime, TimeSpan)", demo_time_and_dates),
        ("GUID and Versioning", demo_guid_and_versioning),
        ("Encoding and Hashing", demo_encoding_and_hashing),
        ("JSON and Data Handling", demo_json_and_data),
        ("Performance and Utilities", demo_performance_and_utilities),
        ("Advanced Console Features", demo_advanced_console),
        ("Interactive Contact Manager", interactive_demo)
    ]
    
    while True:
        Console.WriteLine("Available Demos:")
        for i, (name, _) in enumerate(demos, 1):
            Console.WriteLine(f"{i}. {name}")
        Console.WriteLine(f"{len(demos) + 1}. Run All Demos")
        Console.WriteLine(f"{len(demos) + 2}. Exit")
        Console.WriteLine()
        Console.Write("Choose demo (1-{0}): ".format(len(demos) + 2))
        
        choice = Console.ReadLine()
        Console.WriteLine()
        
        try:
            choice_num = Convert.ToInt32(choice)
            
            if 1 <= choice_num <= len(demos):
                name, demo_func = demos[choice_num - 1]
                Console.WriteLine(f"Running: {name}")
                Console.WriteLine("-" * 40)
                demo_func()
                Console.WriteLine("-" * 40)
                Console.WriteLine("Demo completed! Press Enter to continue...")
                Console.ReadLine()
                Console.Clear()
                
            elif choice_num == len(demos) + 1:
                Console.WriteLine("Running all demos...")
                for name, demo_func in demos[:-1]:  # Skip interactive demo
                    Console.WriteLine(f"\n🎯 {name}")
                    Console.WriteLine("=" * 50)
                    demo_func()
                    Thread.Sleep(2000)  # Pause between demos
                
                Console.WriteLine("\n🎉 All demos completed!")
                Console.WriteLine("Press Enter to return to menu...")
                Console.ReadLine()
                Console.Clear()
                
            elif choice_num == len(demos) + 2:
                Console.WriteLine("Thanks for exploring PySharp 2.1!")
                Console.WriteLine("Happy coding with C# syntax in Python! 🐍➡️C#")
                break
            else:
                Console.WriteError("Invalid choice!")
                
        except:
            Console.WriteError("Please enter a valid number!")
        
        Console.WriteLine()

if __name__ == "__main__":
    main()
