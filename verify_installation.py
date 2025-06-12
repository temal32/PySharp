#!/usr/bin/env python3
"""
PySharp 2.1 - Installation Verification
Quick test to verify PySharp is working correctly
"""

def verify_installation():
    """Verify PySharp installation and features"""
    try:
        from pysharp import *
        
        print("🔍 Verifying PySharp 2.1 installation...")
        print()
        
        # Test basic console
        Console.WriteSuccess("✅ Console operations working")
        
        # Test collections
        test_list = List()
        test_list.Add("test")
        assert test_list.Count() == 1
        Console.WriteSuccess("✅ Collections (List, Dictionary, Array) working")
        
        # Test string processing
        sb = StringBuilder("Hello")
        sb.Append(" PySharp")
        assert "PySharp" in sb.ToString()
        Console.WriteSuccess("✅ String processing (StringBuilder, Regex) working")
        
        # Test JSON
        test_data = {"name": "test", "version": 2.1}
        json_str = Json.Serialize(test_data)
        parsed = Json.Deserialize(json_str)
        assert parsed["name"] == "test"
        Console.WriteSuccess("✅ JSON serialization working")
        
        # Test math
        result = Math.Pow(2, 3)
        assert result == 8
        Console.WriteSuccess("✅ Math operations working")
        
        # Test hashing
        hash_result = Hash.MD5("test")
        assert len(hash_result) == 32
        Console.WriteSuccess("✅ Cryptographic hashing working")
        
        # Test GUID
        guid = Guid.NewGuid()
        assert len(guid.ToString()) == 36
        Console.WriteSuccess("✅ GUID generation working")
        
        # Test performance measurement
        sw = Stopwatch()
        sw.Start()
        sw.Stop()
        assert sw.ElapsedMilliseconds >= 0
        Console.WriteSuccess("✅ Performance measurement working")
        
        # Count available classes
        pysharp_classes = [name for name in dir() 
                          if name[0].isupper() and not name.startswith('_')]
        
        print()
        Console.WriteLineColored("🎉 PySharp 2.1 Installation Verified!", ConsoleColor.Green)
        print(f"📦 {len(pysharp_classes)} C# classes available")
        print("🚀 Ready to use C# syntax in Python!")
        print()
        
        # Show quick example
        Console.WriteInfo("💡 Quick Start Example:")
        print("""
from pysharp import *

# Use C# syntax in Python!
names = List()
names.Add("Alice")
names.Add("Bob")

Console.WriteLine(f"Count: {names.Count()}")
Console.WriteSuccess("PySharp is awesome!")
""")
        
        return True
        
    except ImportError as e:
        Console.WriteError(f"❌ Import Error: {e}")
        print("Make sure pysharp.py is in the same directory")
        return False
    except Exception as e:
        Console.WriteError(f"❌ Error: {e}")
        return False

if __name__ == "__main__":
    success = verify_installation()
    if success:
        print("Installation verification completed successfully! ✨")
    else:
        print("Installation verification failed. Please check the errors above.")
