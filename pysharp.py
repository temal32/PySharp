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
