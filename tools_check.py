import sys
import shutil

print(f"Python Version: {sys.version}")
interpreter_path = sys.executable
print(f"Interpreter Path: {interpreter_path}")
pip_location = shutil.which("pip")
if pip_location:
    print(f"pip Status: Available (Found at: {pip_location})")
else:
    print("pip Status: Not Available")