#!/usr/bin/env python3
"""
PySharp Test Suite
Tests the basic functionality of PySharp classes
"""

from pysharp import *

def test_console():
    """Test Console class"""
    print("Testing Console class...")
    Console.WriteLine("Console.WriteLine() works!")
    Console.Write("Console.Write() works! ")
    Console.WriteLine("(continued)")
    return True

def test_math():
    """Test Math class"""
    print("Testing Math class...")
    assert Math.Max(5, 10) == 10
    assert Math.Min(5, 10) == 5
    assert Math.Abs(-5) == 5
    assert Math.Pow(2, 3) == 8
    assert Math.Round(3.14159, 2) == 3.14
    print("✅ Math tests passed!")
    return True

def test_string():
    """Test String class"""
    print("Testing String class...")
    assert String.IsNullOrEmpty("") == True
    assert String.IsNullOrEmpty("test") == False
    assert String.IsNullOrEmpty(None) == True
    
    joined = String.Join(", ", ["a", "b", "c"])
    assert joined == "a, b, c"
    
    formatted = String.Format("Hello {0}!", "World")
    assert formatted == "Hello World!"
    
    print("✅ String tests passed!")
    return True

def test_convert():
    """Test Convert class"""
    print("Testing Convert class...")
    assert Convert.ToInt32("42") == 42
    assert Convert.ToString(123) == "123"
    assert Convert.ToDouble("3.14") == 3.14
    assert Convert.ToBoolean("true") == True
    assert Convert.ToBoolean("false") == False
    print("✅ Convert tests passed!")
    return True

def test_datetime():
    """Test DateTime class"""
    print("Testing DateTime class...")
    now = DateTime.Now()
    today = DateTime.Today()
    utc_now = DateTime.UtcNow()
    
    assert now is not None
    assert today is not None
    assert utc_now is not None
    print("✅ DateTime tests passed!")
    return True

def test_random():
    """Test Random class"""
    print("Testing Random class...")
    # Test random number generation
    for i in range(10):
        num = rnd.Next(1, 10)
        assert 1 <= num <= 9, f"Random number {num} out of range"
    
    # Test random double
    for i in range(10):
        num = rnd.NextDouble()
        assert 0.0 <= num < 1.0, f"Random double {num} out of range"
    
    print("✅ Random tests passed!")
    return True

def test_file_operations():
    """Test File operations"""
    print("Testing File operations...")
    
    test_file = "test_pysharp.txt"
    test_content = "Hello PySharp!"
    
    # Write file
    File.WriteAllText(test_file, test_content)
    assert File.Exists(test_file), "File was not created"
    
    # Read file
    content = File.ReadAllText(test_file)
    assert content == test_content, f"File content mismatch: {content}"
    
    # Clean up
    File.Delete(test_file)
    assert not File.Exists(test_file), "File was not deleted"
    
    print("✅ File operation tests passed!")
    return True

def test_path_operations():
    """Test Path operations"""
    print("Testing Path operations...")
    
    # Test path combination
    combined = Path.Combine("folder", "subfolder", "file.txt")
    expected = "folder" + os.sep + "subfolder" + os.sep + "file.txt"
    assert combined == expected or combined.replace("/", os.sep) == expected
    
    # Test filename extraction
    filename = Path.GetFileName("folder/file.txt")
    assert filename == "file.txt"
    
    # Test extension
    ext = Path.GetExtension("file.txt")
    assert ext == ".txt"
    
    print("✅ Path operation tests passed!")
    return True

def test_environment():
    """Test Environment operations"""
    print("Testing Environment operations...")
    
    # Test current directory
    current_dir = Environment.CurrentDirectory()
    assert current_dir is not None
    assert len(current_dir) > 0
    
    print("✅ Environment tests passed!")
    return True

def test_array():
    """Test Array class"""
    print("Testing Array class...")
    
    # Test sorting
    test_array = [3, 1, 4, 1, 5]
    Array.Sort(test_array)
    assert test_array == [1, 1, 3, 4, 5]
    
    # Test reverse
    Array.Reverse(test_array)
    assert test_array == [5, 4, 3, 1, 1]
    
    # Test IndexOf
    assert Array.IndexOf(test_array, 4) == 1
    assert Array.IndexOf(test_array, 99) == -1
    
    # Test Contains
    assert Array.Contains(test_array, 4) == True
    assert Array.Contains(test_array, 99) == False
    
    print("✅ Array tests passed!")
    return True

def test_list():
    """Test List class"""
    print("Testing List class...")
    
    # Create list and add items
    my_list = List()
    my_list.Add("apple")
    my_list.Add("banana")
    my_list.Add("cherry")
    
    assert my_list.Count() == 3
    assert my_list.Contains("banana") == True
    assert my_list.IndexOf("cherry") == 2
    
    # Test removal
    my_list.Remove("banana")
    assert my_list.Count() == 2
    assert my_list.Contains("banana") == False
    
    # Test insert
    my_list.Insert(1, "orange")
    assert my_list[1] == "orange"
    
    print("✅ List tests passed!")
    return True

def test_dictionary():
    """Test Dictionary class"""
    print("Testing Dictionary class...")
    
    # Create dictionary and add items
    my_dict = Dictionary()
    my_dict.Add("name", "John")
    my_dict.Add("age", 30)
    my_dict.Add("city", "New York")
    
    assert my_dict.Count() == 3
    assert my_dict.ContainsKey("name") == True
    assert my_dict.ContainsValue("John") == True
    
    # Test TryGetValue
    success, value = my_dict.TryGetValue("name")
    assert success == True
    assert value == "John"
    
    success, value = my_dict.TryGetValue("nonexistent")
    assert success == False
    
    # Test indexer
    my_dict["country"] = "USA"
    assert my_dict["country"] == "USA"
    
    print("✅ Dictionary tests passed!")
    return True

def test_stringbuilder():
    """Test StringBuilder class"""
    print("Testing StringBuilder class...")
    
    sb = StringBuilder("Hello")
    sb.Append(" ")
    sb.Append("World")
    sb.AppendLine("!")
    sb.AppendLine("How are you?")
    
    result = sb.ToString()
    assert "Hello World!" in result
    assert "How are you?" in result
    
    # Test replace
    sb.Replace("World", "PySharp")
    result = sb.ToString()
    assert "PySharp" in result
    
    print("✅ StringBuilder tests passed!")
    return True

def test_regex():
    """Test Regex class"""
    print("Testing Regex class...")
    
    text = "Hello 123 World 456"
    
    # Test IsMatch
    assert Regex.IsMatch(text, r"\d+") == True
    assert Regex.IsMatch(text, r"xyz") == False
    
    # Test Match
    first_number = Regex.Match(text, r"\d+")
    assert first_number == "123"
    
    # Test Matches
    all_numbers = Regex.Matches(text, r"\d+")
    assert all_numbers == ["123", "456"]
    
    # Test Replace
    replaced = Regex.Replace(text, r"\d+", "XXX")
    assert replaced == "Hello XXX World XXX"
    
    print("✅ Regex tests passed!")
    return True

def test_timespan():
    """Test TimeSpan class"""
    print("Testing TimeSpan class...")
    
    # Create TimeSpan
    ts = TimeSpan(days=1, hours=2, minutes=30, seconds=45)
    
    assert ts.Days == 1
    assert ts.Hours == 2
    assert ts.Minutes == 30
    assert ts.Seconds == 45
    
    # Test static methods
    ts_hours = TimeSpan.FromHours(24)
    assert ts_hours.Days == 1
    
    ts_minutes = TimeSpan.FromMinutes(120)
    assert ts_minutes.Hours == 2
    
    print("✅ TimeSpan tests passed!")
    return True

def test_guid():
    """Test Guid class"""
    print("Testing Guid class...")
    
    # Create new GUID
    guid1 = Guid.NewGuid()
    guid2 = Guid.NewGuid()
    
    # Should be different
    assert guid1.ToString() != guid2.ToString()
    
    # Test empty GUID
    empty_guid = Guid.Empty()
    assert empty_guid.ToString() == "00000000-0000-0000-0000-000000000000"
    
    # Test parsing
    guid_string = "550e8400-e29b-41d4-a716-446655440000"
    parsed_guid = Guid(guid_string)
    assert parsed_guid.ToString() == guid_string
    
    print("✅ Guid tests passed!")
    return True

def test_encoding():
    """Test Encoding class"""
    print("Testing Encoding class...")
    
    test_text = "Hello PySharp!"
    
    # Test UTF-8
    utf8_bytes = Encoding.UTF8_GetBytes(test_text)
    decoded_text = Encoding.UTF8_GetString(utf8_bytes)
    assert decoded_text == test_text
    
    # Test Base64
    encoded = Encoding.Base64_Encode(test_text)
    decoded_bytes = Encoding.Base64_Decode(encoded)
    decoded_text = decoded_bytes.decode('utf-8')
    assert decoded_text == test_text
    
    print("✅ Encoding tests passed!")
    return True

def test_hash():
    """Test Hash class"""
    print("Testing Hash class...")
    
    test_data = "Hello PySharp!"
    
    # Test different hash algorithms
    md5_hash = Hash.MD5(test_data)
    sha1_hash = Hash.SHA1(test_data)
    sha256_hash = Hash.SHA256(test_data)
    
    assert len(md5_hash) == 32  # MD5 is 32 hex chars
    assert len(sha1_hash) == 40  # SHA1 is 40 hex chars
    assert len(sha256_hash) == 64  # SHA256 is 64 hex chars
    
    # Same input should produce same hash
    assert Hash.MD5(test_data) == md5_hash
    
    print("✅ Hash tests passed!")
    return True

def test_json():
    """Test Json class"""
    print("Testing Json class...")
    
    # Test object serialization
    test_obj = {"name": "John", "age": 30, "scores": [95, 87, 92]}
    
    json_string = Json.Serialize(test_obj)
    assert "John" in json_string
    assert "30" in json_string
    
    # Test deserialization
    parsed_obj = Json.Deserialize(json_string)
    assert parsed_obj["name"] == "John"
    assert parsed_obj["age"] == 30
    assert parsed_obj["scores"] == [95, 87, 92]
    
    print("✅ Json tests passed!")
    return True

def test_stopwatch():
    """Test Stopwatch class"""
    print("Testing Stopwatch class...")
    
    sw = Stopwatch()
    assert sw.IsRunning == False
    
    sw.Start()
    assert sw.IsRunning == True
    
    Thread.Sleep(100)  # Sleep for 100ms
    
    sw.Stop()
    assert sw.IsRunning == False
    assert sw.ElapsedMilliseconds >= 90  # Allow some tolerance
    
    print("✅ Stopwatch tests passed!")
    return True

def test_version():
    """Test Version class"""
    print("Testing Version class...")
    
    # Create version
    version = Version(2, 1, 0, 0)
    assert version.Major == 2
    assert version.Minor == 1
    assert version.ToString() == "2.1"  # No build/revision shown when 0
    
    # Version with build
    version_with_build = Version(2, 1, 5, 0)
    assert version_with_build.ToString() == "2.1.5"
    
    # Parse version string
    parsed = Version.Parse("3.2.1.4")
    assert parsed.Major == 3
    assert parsed.Minor == 2
    assert parsed.Build == 1
    assert parsed.Revision == 4
    assert parsed.ToString() == "3.2.1.4"
    
    print("✅ Version tests passed!")
    return True

def test_console_colors():
    """Test colored console output"""
    print("Testing Console colors...")
    
    # These should not crash
    Console.WriteError("This is an error message")
    Console.WriteWarning("This is a warning message")
    Console.WriteSuccess("This is a success message")
    Console.WriteInfo("This is an info message")
    Console.WriteColored("This is colored text", ConsoleColor.Blue)
    Console.WriteLine()  # New line after colored text
    
    print("✅ Console color tests passed!")
    return True

def run_all_tests():
    """Run all tests"""
    Console.SetTitle("PySharp Test Suite")
    Console.Clear()
    Console.WriteLine("=== PySharp Test Suite ===")
    Console.WriteLine()
    
    tests = [
        test_console,
        test_math,
        test_string,
        test_convert,
        test_datetime,
        test_random,
        test_file_operations,
        test_path_operations,
        test_environment,
        test_array,
        test_list,
        test_dictionary,
        test_stringbuilder,
        test_regex,
        test_timespan,
        test_guid,
        test_encoding,
        test_hash,
        test_json,
        test_stopwatch,
        test_version,
        test_console_colors
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            if test():
                passed += 1
            else:
                failed += 1
                Console.WriteLine(f"❌ {test.__name__} failed!")
        except Exception as e:
            failed += 1
            Console.WriteLine(f"❌ {test.__name__} failed with error: {e}")
    
    Console.WriteLine()
    Console.WriteLine(f"=== Test Results ===")
    Console.WriteLine(f"✅ Passed: {passed}")
    Console.WriteLine(f"❌ Failed: {failed}")
    Console.WriteLine(f"Total: {passed + failed}")
    
    if failed == 0:
        Console.WriteLine()
        Console.WriteLine("🎉 All tests passed! PySharp is working correctly.")
    else:
        Console.WriteLine()
        Console.WriteLine("⚠️  Some tests failed. Please check the output above.")
    
    return failed == 0

if __name__ == "__main__":
    import os  # Need this for os.sep in tests
    success = run_all_tests()
    Environment.Exit(0 if success else 1)
