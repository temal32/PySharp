class Console:
    def Write(self):
        print(self, end="")
    def WriteLine(self):
        print("\n" + self)
    @staticmethod
    def ReadLine():
        input()
        # saving input in a variable:
        # given_input = input()
    @staticmethod
    def Clear():
        import os as Console
        Console.system("cls")
class Thread:
    def Sleep(self):
        import time
        timetosleep = int(self / 1000)
        time.sleep(timetosleep)
    def Start(self):
        import subprocess
        subprocess.call(self)
class Environment:
    def Exit(self):
        exit(self)
class Process:
    def Start(self):
        import subprocess
        subprocess.call(self)