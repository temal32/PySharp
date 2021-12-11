from pysharp import *

# C# commands in Python 3.9:
Console.Write("Hello World!");
Console.WriteLine("Hello World");
Thread.Sleep(2000); # Do not forget to enter milliseconds as in C#
Console.Clear();
Console.ReadLine(); # Giving arguments to this function will print out an error
Process.Start("cmd.exe");
Thread.Start("cmd.exe");
Environment.Exit(0); # Do not forget to enter an integer as an exit code, useful in if-statements, code after this command will not be executed