"""
Copyright PyCharp Temal © 2021

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
http://www.apache.org/licenses/LICENSE-2.0
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""
# PYSHARP VERSION 2.1 - Extended C# Syntax
import os
import sys
import time
import subprocess
import random
import math
import datetime
import re
import uuid
import json
import base64
import hashlib
import urllib.parse
import socket
from typing import List, Any, Dict
from collections import defaultdict

class Console:
    @staticmethod
    def Write(text=""):
        """Writes text to console without newline"""
        print(str(text), end="")
    
    @staticmethod
    def WriteLine(text=""):
        """Writes text to console with newline"""
        print(str(text))
    
    @staticmethod
    def ReadLine():
        """Reads a line from console input"""
        return input()
    
    @staticmethod
    def ReadKey():
        """Reads a single key press (simplified version)"""
        return input("Press Enter to continue...")
    
    @staticmethod
    def Clear():
        """Clears the console screen"""
        os.system("cls" if os.name == "nt" else "clear")
    
    @staticmethod
    def Beep():
        """Makes a beep sound"""
        print("\a")
    
    @staticmethod
    def SetTitle(title):
        """Sets the console window title"""
        if os.name == "nt":
            os.system(f'title {title}')
        else:
            print(f'\033]0;{title}\007', end='')

class Thread:
    @staticmethod
    def Sleep(milliseconds):
        """Sleeps for specified milliseconds"""
        time.sleep(milliseconds / 1000.0)
    
    @staticmethod
    def Start(command):
        """Starts a new process"""
        subprocess.Popen(command, shell=True)

class Environment:
    @staticmethod
    def Exit(code=0):
        """Exits the program with specified exit code"""
        sys.exit(code)
    
    @staticmethod
    def GetEnvironmentVariable(name):
        """Gets an environment variable"""
        return os.environ.get(name)
    
    @staticmethod
    def SetEnvironmentVariable(name, value):
        """Sets an environment variable"""
        os.environ[name] = value
    
    @staticmethod
    def CurrentDirectory():
        """Gets current directory"""
        return os.getcwd()
    
    @staticmethod
    def ChangeDirectory(path):
        """Changes current directory"""
        os.chdir(path)

class Process:
    @staticmethod
    def Start(command):
        """Starts a new process and waits for completion"""
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        return result.returncode
    
    @staticmethod
    def StartAsync(command):
        """Starts a new process asynchronously"""
        return subprocess.Popen(command, shell=True)
    
    @staticmethod
    def GetCurrentProcess():
        """Gets current process ID"""
        return os.getpid()

class DateTime:
    @staticmethod
    def Now():
        """Gets current date and time"""
        return datetime.datetime.now()
    
    @staticmethod
    def Today():
        """Gets today's date"""
        return datetime.date.today()
    
    @staticmethod
    def UtcNow():
        """Gets current UTC date and time"""
        return datetime.datetime.utcnow()

class Math:
    @staticmethod
    def Abs(value):
        """Returns absolute value"""
        return abs(value)
    
    @staticmethod
    def Max(a, b):
        """Returns maximum of two values"""
        return max(a, b)
    
    @staticmethod
    def Min(a, b):
        """Returns minimum of two values"""
        return min(a, b)
    
    @staticmethod
    def Pow(base, exponent):
        """Returns base raised to exponent"""
        return math.pow(base, exponent)
    
    @staticmethod
    def Sqrt(value):
        """Returns square root"""
        return math.sqrt(value)
    
    @staticmethod
    def Round(value, decimals=0):
        """Rounds to specified decimal places"""
        return round(value, decimals)
    
    @staticmethod
    def Floor(value):
        """Returns floor of value"""
        return math.floor(value)
    
    @staticmethod
    def Ceiling(value):
        """Returns ceiling of value"""
        return math.ceil(value)
    
    PI = math.pi
    E = math.e

class Random:
    def __init__(self):
        self._random = random.Random()
    
    def Next(self, min_val=0, max_val=2147483647):
        """Returns random integer between min and max"""
        return self._random.randint(min_val, max_val - 1)
    
    def NextDouble(self):
        """Returns random double between 0.0 and 1.0"""
        return self._random.random()
    
    def NextBytes(self, byte_array):
        """Fills byte array with random bytes"""
        for i in range(len(byte_array)):
            byte_array[i] = self._random.randint(0, 255)

class String:
    @staticmethod
    def IsNullOrEmpty(value):
        """Checks if string is null or empty"""
        return value is None or value == ""
    
    @staticmethod
    def IsNullOrWhiteSpace(value):
        """Checks if string is null, empty, or whitespace"""
        return value is None or value.strip() == ""
    
    @staticmethod
    def Join(separator, values):
        """Joins array of strings with separator"""
        return separator.join(str(v) for v in values)
    
    @staticmethod
    def Format(format_string, *args):
        """Formats string with arguments"""
        return format_string.format(*args)

class Convert:
    @staticmethod
    def ToInt32(value):
        """Converts value to 32-bit integer"""
        return int(value)
    
    @staticmethod
    def ToDouble(value):
        """Converts value to double"""
        return float(value)
    
    @staticmethod
    def ToString(value):
        """Converts value to string"""
        return str(value)
    
    @staticmethod
    def ToBoolean(value):
        """Converts value to boolean"""
        if isinstance(value, str):
            return value.lower() in ('true', '1', 'yes', 'on')
        return bool(value)

class File:
    @staticmethod
    def Exists(path):
        """Checks if file exists"""
        return os.path.isfile(path)
    
    @staticmethod
    def ReadAllText(path):
        """Reads entire file as text"""
        with open(path, 'r', encoding='utf-8') as f:
            return f.read()
    
    @staticmethod
    def WriteAllText(path, content):
        """Writes text to file"""
        with open(path, 'w', encoding='utf-8') as f:
            f.write(content)
    
    @staticmethod
    def ReadAllLines(path):
        """Reads all lines from file"""
        with open(path, 'r', encoding='utf-8') as f:
            return f.readlines()
    
    @staticmethod
    def WriteAllLines(path, lines):
        """Writes lines to file"""
        with open(path, 'w', encoding='utf-8') as f:
            f.writelines(lines)
    
    @staticmethod
    def Delete(path):
        """Deletes file"""
        os.remove(path)
    
    @staticmethod
    def Copy(source, destination):
        """Copies file"""
        import shutil
        shutil.copy2(source, destination)

class Directory:
    @staticmethod
    def Exists(path):
        """Checks if directory exists"""
        return os.path.isdir(path)
    
    @staticmethod
    def CreateDirectory(path):
        """Creates directory"""
        os.makedirs(path, exist_ok=True)
    
    @staticmethod
    def Delete(path, recursive=False):
        """Deletes directory"""
        if recursive:
            import shutil
            shutil.rmtree(path)
        else:
            os.rmdir(path)
    
    @staticmethod
    def GetFiles(path, pattern="*"):
        """Gets files in directory"""
        import glob
        return glob.glob(os.path.join(path, pattern))
    
    @staticmethod
    def GetDirectories(path):
        """Gets subdirectories"""
        return [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))]

class Path:
    @staticmethod
    def Combine(*paths):
        """Combines path components"""
        return os.path.join(*paths)
    
    @staticmethod
    def GetFileName(path):
        """Gets file name from path"""
        return os.path.basename(path)
    
    @staticmethod
    def GetDirectoryName(path):
        """Gets directory name from path"""
        return os.path.dirname(path)
    
    @staticmethod
    def GetExtension(path):
        """Gets file extension"""
        return os.path.splitext(path)[1]
    
    @staticmethod
    def GetFileNameWithoutExtension(path):
        """Gets file name without extension"""
        return os.path.splitext(os.path.basename(path))[0]

# Create global instances for classes that need them
rnd = Random()

class Array:
    @staticmethod
    def Sort(arr):
        """Sorts an array in-place"""
        arr.sort()
        return arr
    
    @staticmethod
    def Reverse(arr):
        """Reverses an array in-place"""
        arr.reverse()
        return arr
    
    @staticmethod
    def IndexOf(arr, value):
        """Finds index of value in array"""
        try:
            return arr.index(value)
        except ValueError:
            return -1
    
    @staticmethod
    def LastIndexOf(arr, value):
        """Finds last index of value in array"""
        try:
            return len(arr) - 1 - arr[::-1].index(value)
        except ValueError:
            return -1
    
    @staticmethod
    def Contains(arr, value):
        """Checks if array contains value"""
        return value in arr
    
    @staticmethod
    def Clear(arr):
        """Clears all elements from array"""
        arr.clear()
    
    @staticmethod
    def Copy(source, destination, length):
        """Copies elements from source to destination"""
        for i in range(length):
            if i < len(source) and i < len(destination):
                destination[i] = source[i]
    
    @staticmethod
    def Resize(arr, new_size):
        """Resizes array to new size"""
        while len(arr) < new_size:
            arr.append(None)
        while len(arr) > new_size:
            arr.pop()

class List:
    def __init__(self):
        self._items = []
    
    def Add(self, item):
        """Adds item to list"""
        self._items.append(item)
    
    def Remove(self, item):
        """Removes first occurrence of item"""
        try:
            self._items.remove(item)
            return True
        except ValueError:
            return False
    
    def RemoveAt(self, index):
        """Removes item at specified index"""
        if 0 <= index < len(self._items):
            del self._items[index]
    
    def Insert(self, index, item):
        """Inserts item at specified index"""
        self._items.insert(index, item)
    
    def Clear(self):
        """Removes all items"""
        self._items.clear()
    
    def Contains(self, item):
        """Checks if list contains item"""
        return item in self._items
    
    def IndexOf(self, item):
        """Gets index of item"""
        try:
            return self._items.index(item)
        except ValueError:
            return -1
    
    def Count(self):
        """Gets number of items"""
        return len(self._items)
    
    def ToArray(self):
        """Converts to array"""
        return self._items.copy()
    
    def Sort(self):
        """Sorts the list"""
        self._items.sort()
    
    def Reverse(self):
        """Reverses the list"""
        self._items.reverse()
    
    def __getitem__(self, index):
        return self._items[index]
    
    def __setitem__(self, index, value):
        self._items[index] = value
    
    def __len__(self):
        return len(self._items)

class Dictionary:
    def __init__(self):
        self._items = {}
    
    def Add(self, key, value):
        """Adds key-value pair"""
        if key in self._items:
            raise KeyError(f"Key '{key}' already exists")
        self._items[key] = value
    
    def Remove(self, key):
        """Removes key-value pair"""
        if key in self._items:
            del self._items[key]
            return True
        return False
    
    def ContainsKey(self, key):
        """Checks if dictionary contains key"""
        return key in self._items
    
    def ContainsValue(self, value):
        """Checks if dictionary contains value"""
        return value in self._items.values()
    
    def TryGetValue(self, key):
        """Tries to get value, returns (success, value)"""
        if key in self._items:
            return (True, self._items[key])
        return (False, None)
    
    def Clear(self):
        """Removes all items"""
        self._items.clear()
    
    def Count(self):
        """Gets number of items"""
        return len(self._items)
    
    def Keys(self):
        """Gets all keys"""
        return list(self._items.keys())
    
    def Values(self):
        """Gets all values"""
        return list(self._items.values())
    
    def __getitem__(self, key):
        return self._items[key]
    
    def __setitem__(self, key, value):
        self._items[key] = value
    
    def __contains__(self, key):
        return key in self._items

class StringBuilder:
    def __init__(self, initial_value=""):
        self._buffer = [initial_value] if initial_value else []
    
    def Append(self, text):
        """Appends text to buffer"""
        self._buffer.append(str(text))
        return self
    
    def AppendLine(self, text=""):
        """Appends text with newline"""
        self._buffer.append(str(text) + "\n")
        return self
    
    def Insert(self, index, text):
        """Inserts text at position"""
        current = self.ToString()
        new_text = current[:index] + str(text) + current[index:]
        self._buffer = [new_text]
        return self
    
    def Remove(self, start, length):
        """Removes characters"""
        current = self.ToString()
        new_text = current[:start] + current[start + length:]
        self._buffer = [new_text]
        return self
    
    def Replace(self, old_value, new_value):
        """Replaces all occurrences"""
        current = self.ToString()
        new_text = current.replace(old_value, new_value)
        self._buffer = [new_text]
        return self
    
    def Clear(self):
        """Clears the buffer"""
        self._buffer.clear()
        return self
    
    def ToString(self):
        """Converts to string"""
        return "".join(self._buffer)
    
    def Length(self):
        """Gets total length"""
        return len(self.ToString())

class Regex:
    @staticmethod
    def IsMatch(input_text, pattern):
        """Checks if pattern matches input"""
        return bool(re.search(pattern, input_text))
    
    @staticmethod
    def Match(input_text, pattern):
        """Gets first match"""
        match = re.search(pattern, input_text)
        return match.group(0) if match else ""
    
    @staticmethod
    def Matches(input_text, pattern):
        """Gets all matches"""
        return re.findall(pattern, input_text)
    
    @staticmethod
    def Replace(input_text, pattern, replacement):
        """Replaces matches with replacement"""
        return re.sub(pattern, replacement, input_text)
    
    @staticmethod
    def Split(input_text, pattern):
        """Splits string by pattern"""
        return re.split(pattern, input_text)

class TimeSpan:
    def __init__(self, days=0, hours=0, minutes=0, seconds=0, milliseconds=0):
        self._total_seconds = (days * 24 * 3600 + 
                             hours * 3600 + 
                             minutes * 60 + 
                             seconds + 
                             milliseconds / 1000.0)
    
    @property
    def Days(self):
        return int(self._total_seconds // (24 * 3600))
    
    @property
    def Hours(self):
        return int((self._total_seconds % (24 * 3600)) // 3600)
    
    @property
    def Minutes(self):
        return int((self._total_seconds % 3600) // 60)
    
    @property
    def Seconds(self):
        return int(self._total_seconds % 60)
    
    @property
    def Milliseconds(self):
        return int((self._total_seconds % 1) * 1000)
    
    @property
    def TotalDays(self):
        return self._total_seconds / (24 * 3600)
    
    @property
    def TotalHours(self):
        return self._total_seconds / 3600
    
    @property
    def TotalMinutes(self):
        return self._total_seconds / 60
    
    @property
    def TotalSeconds(self):
        return self._total_seconds
    
    @property
    def TotalMilliseconds(self):
        return self._total_seconds * 1000
    
    def ToString(self):
        return f"{self.Days}.{self.Hours:02d}:{self.Minutes:02d}:{self.Seconds:02d}"
    
    @staticmethod
    def FromDays(days):
        return TimeSpan(days=days)
    
    @staticmethod
    def FromHours(hours):
        return TimeSpan(hours=hours)
    
    @staticmethod
    def FromMinutes(minutes):
        return TimeSpan(minutes=minutes)
    
    @staticmethod
    def FromSeconds(seconds):
        return TimeSpan(seconds=seconds)

class Guid:
    def __init__(self, guid_string=None):
        if guid_string:
            self._guid = uuid.UUID(guid_string)
        else:
            self._guid = uuid.uuid4()
    
    def ToString(self):
        return str(self._guid)
    
    @staticmethod
    def NewGuid():
        return Guid()
    
    @staticmethod
    def Empty():
        return Guid("00000000-0000-0000-0000-000000000000")

class Encoding:
    @staticmethod
    def UTF8_GetBytes(text):
        """Converts string to UTF-8 bytes"""
        return text.encode('utf-8')
    
    @staticmethod
    def UTF8_GetString(bytes_data):
        """Converts UTF-8 bytes to string"""
        return bytes_data.decode('utf-8')
    
    @staticmethod
    def ASCII_GetBytes(text):
        """Converts string to ASCII bytes"""
        return text.encode('ascii')
    
    @staticmethod
    def ASCII_GetString(bytes_data):
        """Converts ASCII bytes to string"""
        return bytes_data.decode('ascii')
    
    @staticmethod
    def Base64_Encode(data):
        """Encodes data to Base64"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return base64.b64encode(data).decode('ascii')
    
    @staticmethod
    def Base64_Decode(encoded_data):
        """Decodes Base64 data"""
        return base64.b64decode(encoded_data)

class Hash:
    @staticmethod
    def MD5(data):
        """Computes MD5 hash"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.md5(data).hexdigest()
    
    @staticmethod
    def SHA1(data):
        """Computes SHA1 hash"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha1(data).hexdigest()
    
    @staticmethod
    def SHA256(data):
        """Computes SHA256 hash"""
        if isinstance(data, str):
            data = data.encode('utf-8')
        return hashlib.sha256(data).hexdigest()

class Uri:
    @staticmethod
    def EscapeDataString(data):
        """URL encodes string"""
        return urllib.parse.quote(data)
    
    @staticmethod
    def UnescapeDataString(data):
        """URL decodes string"""
        return urllib.parse.unquote(data)
    
    @staticmethod
    def IsWellFormedUriString(uri_string):
        """Checks if URI is well-formed"""
        try:
            result = urllib.parse.urlparse(uri_string)
            return all([result.scheme, result.netloc])
        except:
            return False

class Json:
    @staticmethod
    def Serialize(obj):
        """Serializes object to JSON string"""
        return json.dumps(obj, default=str)
    
    @staticmethod
    def Deserialize(json_string):
        """Deserializes JSON string to object"""
        return json.loads(json_string)
    
    @staticmethod
    def SerializeIndented(obj):
        """Serializes object to formatted JSON"""
        return json.dumps(obj, indent=2, default=str)

class Network:
    @staticmethod
    def GetLocalIPAddress():
        """Gets local IP address"""
        try:
            # Connect to a remote address to determine local IP
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except:
            return "127.0.0.1"
    
    @staticmethod
    def GetHostName():
        """Gets computer hostname"""
        return socket.gethostname()
    
    @staticmethod
    def Ping(host, timeout=3):
        """Pings a host (simplified)"""
        if os.name == "nt":
            command = f"ping -n 1 -w {timeout*1000} {host}"
        else:
            command = f"ping -c 1 -W {timeout} {host}"
        
        result = subprocess.run(command, shell=True, 
                               capture_output=True, text=True)
        return result.returncode == 0

class Stopwatch:
    def __init__(self):
        self._start_time = None
        self._elapsed_time = 0
        self._is_running = False
    
    def Start(self):
        """Starts the stopwatch"""
        if not self._is_running:
            self._start_time = time.time()
            self._is_running = True
    
    def Stop(self):
        """Stops the stopwatch"""
        if self._is_running:
            self._elapsed_time += time.time() - self._start_time
            self._is_running = False
    
    def Reset(self):
        """Resets the stopwatch"""
        self._elapsed_time = 0
        self._start_time = None
        self._is_running = False
    
    def Restart(self):
        """Resets and starts the stopwatch"""
        self.Reset()
        self.Start()
    
    @property
    def ElapsedMilliseconds(self):
        """Gets elapsed time in milliseconds"""
        current_elapsed = self._elapsed_time
        if self._is_running:
            current_elapsed += time.time() - self._start_time
        return int(current_elapsed * 1000)
    
    @property
    def ElapsedSeconds(self):
        """Gets elapsed time in seconds"""
        return self.ElapsedMilliseconds / 1000.0
    
    @property
    def IsRunning(self):
        """Gets whether stopwatch is running"""
        return self._is_running

class Version:
    def __init__(self, major=0, minor=0, build=0, revision=0):
        self.Major = major
        self.Minor = minor
        self.Build = build
        self.Revision = revision
    
    def ToString(self):
        if self.Revision > 0:
            return f"{self.Major}.{self.Minor}.{self.Build}.{self.Revision}"
        elif self.Build > 0:
            return f"{self.Major}.{self.Minor}.{self.Build}"
        else:
            return f"{self.Major}.{self.Minor}"
    
    @staticmethod
    def Parse(version_string):
        parts = version_string.split('.')
        major = int(parts[0]) if len(parts) > 0 else 0
        minor = int(parts[1]) if len(parts) > 1 else 0
        build = int(parts[2]) if len(parts) > 2 else 0
        revision = int(parts[3]) if len(parts) > 3 else 0
        return Version(major, minor, build, revision)

class BitConverter:
    @staticmethod
    def GetBytes(value):
        """Converts value to byte array"""
        if isinstance(value, int):
            return value.to_bytes(4, byteorder='little')
        elif isinstance(value, float):
            import struct
            return struct.pack('<f', value)
        elif isinstance(value, bool):
            return b'\x01' if value else b'\x00'
        else:
            return str(value).encode('utf-8')
    
    @staticmethod
    def ToInt32(bytes_data, start_index=0):
        """Converts bytes to 32-bit integer"""
        return int.from_bytes(bytes_data[start_index:start_index+4], 
                             byteorder='little')
    
    @staticmethod
    def ToString(bytes_data, separator="-"):
        """Converts bytes to hex string"""
        return separator.join(f'{b:02X}' for b in bytes_data)

class Enum:
    @staticmethod
    def GetNames(enum_class):
        """Gets all enum names"""
        return [name for name in dir(enum_class) 
                if not name.startswith('_')]
    
    @staticmethod
    def GetValues(enum_class):
        """Gets all enum values"""
        return [getattr(enum_class, name) for name in dir(enum_class) 
                if not name.startswith('_')]
    
    @staticmethod
    def Parse(enum_class, name):
        """Parses enum from string"""
        return getattr(enum_class, name)

class ConsoleColor:
    """Console color constants"""
    Black = "\033[30m"
    DarkBlue = "\033[34m"
    DarkGreen = "\033[32m"
    DarkCyan = "\033[36m"
    DarkRed = "\033[31m"
    DarkMagenta = "\033[35m"
    DarkYellow = "\033[33m"
    Gray = "\033[37m"
    DarkGray = "\033[90m"
    Blue = "\033[94m"
    Green = "\033[92m"
    Cyan = "\033[96m"
    Red = "\033[91m"
    Magenta = "\033[95m"
    Yellow = "\033[93m"
    White = "\033[97m"
    Reset = "\033[0m"

# Enhanced Console class with colors
class ColorConsole:
    @staticmethod
    def WriteLineColored(text, color=ConsoleColor.White):
        """Writes colored text with newline"""
        print(f"{color}{text}{ConsoleColor.Reset}")
    
    @staticmethod
    def WriteColored(text, color=ConsoleColor.White):
        """Writes colored text without newline"""
        print(f"{color}{text}{ConsoleColor.Reset}", end="")
    
    @staticmethod
    def WriteError(text):
        """Writes error in red"""
        ColorConsole.WriteLineColored(text, ConsoleColor.Red)
    
    @staticmethod
    def WriteWarning(text):
        """Writes warning in yellow"""
        ColorConsole.WriteLineColored(text, ConsoleColor.Yellow)
    
    @staticmethod
    def WriteSuccess(text):
        """Writes success in green"""
        ColorConsole.WriteLineColored(text, ConsoleColor.Green)
    
    @staticmethod
    def WriteInfo(text):
        """Writes info in cyan"""
        ColorConsole.WriteLineColored(text, ConsoleColor.Cyan)

# Add convenience methods to main Console class
Console.WriteError = ColorConsole.WriteError
Console.WriteWarning = ColorConsole.WriteWarning
Console.WriteSuccess = ColorConsole.WriteSuccess
Console.WriteInfo = ColorConsole.WriteInfo
Console.WriteColored = ColorConsole.WriteColored
Console.WriteLineColored = ColorConsole.WriteLineColored
