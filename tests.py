from functions.run_python_file import run_python_file as run

print(run("calculator", "main.py"))
print(run("calculator", "main.py", ["3 + 5"]))
print(run("calculator", "tests.py"))
print(run("calculator", "../main.py"))
print(run("calculator", "nonexistent.py"))
